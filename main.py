from vault import Vault

def prompt_nonempty(label: str) -> str:
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print("Boş olamaz.")

def main():
    v = Vault("vault.json")

    while True:
        print("\n=== Simple Vault ===")
        print("1) Add")
        print("2) List")
        print("3) Get")
        print("4) Delete")
        print("5) Generate password")
        print("6) Exit")

        choice = input("Seçim: ").strip()

        if choice == "1":
            v.unlock()
            site = prompt_nonempty("Site (örn: github)")
            username = prompt_nonempty("Username")
            password = prompt_nonempty("Şifre")
            v.add(site, username, password)
            print("✅ Eklendi.")

        elif choice == "2":
            v.unlock()
            items = v.list_items()
            if not items:
                print("Vault boş.")
            else:
                print("Kayıtlar:")
                for it in items:
                    print(f"- {it['site']} | {it['username']}")

        elif choice == "3":
            v.unlock()
            site = prompt_nonempty("Site")
            username = prompt_nonempty("Username")
            pw = v.get(site, username)
            if pw is None:
                print("Bulunamadı.")
            else:
                print(f"Şifre: {pw}")

        elif choice == "4":
            v.unlock()
            site = prompt_nonempty("Site")
            username = prompt_nonempty("Username")
            ok = v.delete(site, username)
            print("✅ Silindi." if ok else "Bulunamadı.")

        elif choice == "5":
            length_str = input("Uzunluk (örn 16) [varsayılan 16]: ").strip()
            length = int(length_str) if length_str else 16
            print("Üretilen:", Vault.generate(length))

        elif choice == "6":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
