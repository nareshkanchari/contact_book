import sqlite3


print("*****************************************welcome to phone book*****************************************************\n")


def phone_book():
    try:
        conn = sqlite3.connect("phonebook.sqlite3")
        cur = conn.cursor()
    except:
        print("something went wrong please try again")

    def view():
        try:
            while True:
                print(
                    "1.create new contact\n2.update contact\n3.view contact\n4.delete contact\n5.exit")

                choice = int(input("Enter your choice: "))
                if choice == 1:
                    create_contact()
                elif choice == 2:
                    update_contact()
                elif choice == 3:
                    view_contact()
                elif choice == 4:
                    delete_contact()
                elif choice == 5:
                    break
                else:
                    print("please enter correct choice")
        except Exception as e:
            print(e)

    def create_contact():
        name = input("Enter name: ")
        addr = input("Enter address: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS phonebook(cno number  primary key, name text, addr text, phone text, email email)")
        cur.execute("select max(cno) from phonebook")
        res = cur.fetchone()
        # print(res)
        if res[0]:
            cno = res[0] + 1
        else:
            cno = 1001
        cur.execute("insert into phonebook values (?,?,?,?,?)",
                    (cno, name, addr, phone, email))
        conn.commit()
        print("\nData inserted successfully\n")

    def update_contact():
        name = input("enter contact name to update: ")
        print("")
        fetchdata = cur.execute(
            "select * from phonebook where name=?", (name,))
        # print(cur.fetchone())
        if cur.fetchone():
            fetchdata = cur.execute(
                "select * from phonebook where name=?", (name,))
            list_ = []
            for row in fetchdata:
                for col in row:
                    list_.append(col)

            for i in range(1, len(list_)):
                print(i, list_[i])

            # print(
            #     f"\nname: {list_[1]}\naddres: {list_[2]}\nphone_number: {list_[3]}\nemail: {list_[4]}\n")

            choice = int(
                input("\nenter number which one you want to update: "))
            if choice == 1:
                name = input("enter name: ")
                cid = list_[0]
                cur.execute(
                    "update phonebook set name= ? where cno = ?", (name, cid))
                conn.commit()
                print("\nData updated successfully\n")
            elif choice == 2:
                address = input("enter address: ")
                cid = list_[0]
                cur.execute(
                    "update phonebook set addr= ? where cno = ?", (address, cid))
                conn.commit()
                print("\nData updated successfully\n")

            elif choice == 3:
                phone_number = input("enter phone: ")
                cid = list_[0]
                cur.execute(
                    "update phonebook set phone= ? where cno = ?", (phone_number, cid))
                conn.commit()
                print("\nData updated successfully\n")

            elif choice == 4:
                email = input("enter email: ")
                cid = list_[0]
                cur.execute(
                    "update phonebook set email= ? where cno = ?", (email, cid))
                conn.commit()
                print("\nData updated successfully\n")
        else:
            print("\nThat data is not avaialble")

    def view_contact():
        cur.execute('SELECT * FROM phonebook')
        data = cur.fetchall()
        list_ = []
        for row in data:
            print(f"\n{row[1:]}\n")
            # # print(row)
            # for col in row:
            #     list_.append(col)

        # for i in range(1, len(list_)):
        #     print(f" {list_[i]} ", end="")
        conn.commit()

    def delete_contact():
        name1 = input('enter your name: ')
        cur.execute("DELETE from phonebook where name =?", (name1,))
        conn.commit()
        print("\ndata deleted")

    view()


if __name__ == "__main__":
    phone_book()
