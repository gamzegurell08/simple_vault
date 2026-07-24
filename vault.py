import os
import json
import base64
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

VAULT_FILE = "vault.json"
SALT_LEN = 16

KDF_PARAMS = {"n": 2**14, "r": 8, "p": 1}


class Vault:
    def __init__(self, vault_file: str = VAULT_FILE):
        self.vault_file = vault_file
        self.master_password = None

    def _load_raw(self) -> dict | None:
        if not os.path.exists(self.vault_file):
            return None
        with open(self.vault_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_raw(self, data: dict) -> None:
        with open(self.vault_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _init_if_needed(self) -> dict:
        raw = self._load_raw()
        if raw is not None:
            return raw

        salt = os.urandom(SALT_LEN)
        raw = {
            "salt": base64.b64encode(salt).decode("utf-8"),
            "data": None,
        }
        self._save_raw(raw)
        return raw

    def _derive_key(self, master_password: str, salt: bytes) -> bytes:
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=KDF_PARAMS["n"],
            r=KDF_PARAMS["r"],
            p=KDF_PARAMS["p"],
        )
        key = kdf.derive(master_password.encode("utf-8"))
        return base64.urlsafe_b64encode(key)

    def _get_cipher(self, master_password: str, salt: bytes) -> Fernet:
        return Fernet(self._derive_key(master_password, salt))

    def unlock(self) -> None:
        """Menüyü açınca 1 kere şifre sorar, oturum boyunca saklar."""
        if self.master_password is None:
            self.master_password = getpass("Master password: ")

    def _decrypt_vault(self) -> dict:
        raw = self._init_if_needed()
        salt = base64.b64decode(raw["salt"])

        if raw["data"] is None:
            return {}

        cipher = self._get_cipher(self.master_password, salt)
        plaintext = cipher.decrypt(raw["data"].encode("utf-8")).decode("utf-8")
        return json.loads(plaintext)

    def _encrypt_and_save(self, data: dict) -> None:
        raw = self._init_if_needed()
        salt = base64.b64decode(raw["salt"])

        cipher = self._get_cipher(self.master_password, salt)
        plaintext = json.dumps(data, ensure_ascii=False)
        raw["data"] = cipher.encrypt(plaintext.encode("utf-8")).decode("utf-8")

        self._save_raw(raw)

    @staticmethod
    def _key(site: str, username: str) -> str:
        return f"{site} | {username}"

    def add(self, site: str, username: str, password: str) -> None:
        vault = self._decrypt_vault()
        k = self._key(site, username)
        vault[k] = {"site": site, "username": username, "password": password}
        self._encrypt_and_save(vault)

    def list_items(self) -> list[dict]:
        vault = self._decrypt_vault()
        items = []
        for _, v in vault.items():
            items.append(v)
        return items

    def get(self, site: str, username: str) -> str | None:
        vault = self._decrypt_vault()
        k = self._key(site, username)
        if k not in vault:
            return None
        return vault[k]["password"]

    def delete(self, site: str, username: str) -> bool:
        vault = self._decrypt_vault()
        k = self._key(site, username)
        if k not in vault:
            return False
        del vault[k]
        self._encrypt_and_save(vault)
        return True

    @staticmethod
    def generate(length: int = 16) -> str:
        import secrets
        import string

        chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.?/"
        return "".join(secrets.choice(chars) for _ in range(length))
