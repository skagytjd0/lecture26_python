classDiagram
    direction TOTAL
    
    %% --- Core Domain Entities ---
    class Book {
        -book_no: String
        -title: String
        -author: String
        -price: int
        -stock: int
        +get_book_no() String
        +get_title() String
        +get_author() String
        +get_price() int
        +get_stock() int
        +set_book_no(book_no)
        +set_stock(stock)
        +__str__() String
    }

    class Cart {
        -member_id: String
        -book_no: String
        -title: String
        -qty: int
        -price: int
        +get_member_id() String
        +get_book_no() String
        +get_title() String
        +get_qty() int
        +get_price() int
        +set_qty(qty)
        +__str__() String
    }

    %% --- Data Access Objects (DAIs) ---
    class BookDAO {
        -bookDB: dict [book_no: Book]
        +insert_book(book) bool
        +select_book_by_book_no(book_no) Book
        +select_all_books() list~Book~
        +update_book(book_no, book) bool
        +delete_book(book_no) bool
    }

    class CartDAO {
        -cartDB: dict [member_id: list~Cart~]
        +insert_cart_item(cart_item) bool
        +select_cart_by_member(member_id) list~Cart~
        +delete_cart_item(member_id, book_no) bool
        +clear_member_cart(member_id) bool
    }

    %% --- Services ---
    class BookService {
        +book_no_seq: int$
        -dao: BookDAO
        +create_book(book) bool
        +get_all_books() list~Book~
        +get_book_info(book_no) Book
        +update_book_stock(book_no, qty, order_type) bool
        -__init_default_books()
    }

    class CartService {
        -dao: CartDAO
        +add_to_cart(cart_item) bool
        +get_cart_list(member_id) list~Cart~
        +remove_item(member_id, book_no) bool
        +clear_cart(member_id) bool
    }

    %% --- Main Controller / View ---
    class ConsoleBookstore {
        +start_menu: list$
        +user_menu: list$
        +cart_menu: list$
        +user_inquiry_menu: list$
        +member_myinfo_menu: list$
        +admin_menu: list$
        +admin_book_menu: list$
        +admin_member_menu: list$
        +admin_inquiry_menu: list$
        +msv: MemberService
        +bsv: BookService
        +csv: CartService
        +isv: InquiryService
        +main()
        +show_welcome()
        +say_goodbye()
        +select_menu(menu_list) int
        +run_start_menu()
        +menu_join()
        +menu_login()
        +run_user_menu()
        +menu_list_books()
        +run_cart_menu()
        +menu_view_cart()
        +menu_add_cart()
        +menu_remove_cart_item()
        +menu_checkout_cart()
        +menu_order_book()
        +run_user_inquiry_menu()
        +menu_register_inquiry()
        +menu_list_my_inquiries()
        +run_my_info_menu()
        +menu_update_password()
        +menu_delete_membership()
        +run_admin_menu()
        +run_admin_book_menu()
        +menu_register_book()
        +run_admin_member_menu()
        +menu_list_members()
        +menu_view_member_info()
        +menu_delete_member()
        +run_admin_inquiry_menu()
        +menu_list_all_inquiries()
        +menu_answer_inquiry()
    }

    %% --- Relationships ---
    BookDAO --> Book : Manages / Stores
    CartDAO --> Cart : Manages / Stores
    BookService --> BookDAO : Uses
    CartService --> CartDAO : Uses
    ConsoleBookstore --> BookService : Controls
    ConsoleBookstore --> CartService : Controls
    ConsoleBookstore ..> Book : Instantiates
    ConsoleBookstore ..> Cart : Instantiates
