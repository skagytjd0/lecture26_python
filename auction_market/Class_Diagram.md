```mermaid
classDiagram
    %% ==================== APP LAYER ====================
    class ConsoleMarket {
        +start_menu : list
        +user_menu : list
        +admin_menu : list
        -usv : UserService
        -isv : ItemService
        -bsv : BidService
        -wsv : WinningService
        -qsv : InquiryService
        +main() void
        +select_menu(menu_list) int
        +menu_join() void
        +menu_login() void
        +menu_my_info() void
        +menu_update_my_info() void
        +menu_withdraw() void
        +menu_list_users() void
        +menu_admin_update_user() void
        +menu_kick_user() void
        +menu_register_item() void
        +menu_list_items() void
        +menu_cancel_order() void
        +menu_place_bid() void
        +menu_my_bids() void
        +menu_item_bids() void
        +menu_cancel_bid() void
        +menu_close_auction() void
        +menu_my_winnings() void
        +menu_all_winnings() void
        +menu_cancel_winning() void
        +menu_add_inquiry() void
        +menu_my_inquiries() void
        +menu_all_inquiries() void
        +menu_answer_inquiry() void
    }

    %% ==================== USER DOMAIN ====================
    class User {
        -__user_no : int
        -__id : String
        -__password : String
        -__name : String
        -__mobile : String
        -__email : String
        -__address : String
        +get_user_no() int
        +get_id() String
        +get_password() String
        +get_name() String
        +get_mobile() String
        +get_email() String
        +get_address() String
        +set_password(password) void
        +set_name(name) void
        +set_mobile(mobile) void
        +set_email(email) void
        +set_address(address) void
        +__str__() String
    }
    class UserDAO {
        -__memberDB : dict
        +insert_user(user) bool
        +is_exist(id) bool
        +get_user_info(id) User
        +get_all_users() list
        +remove_user(id) bool
    }
    class UserService {
        +ADMIN_ID : String
        +ADMIN_PASSWORD : String
        +user_seq : int
        +current_user : String
        -__dao : UserDAO
        +join(user) bool
        +login(id, password) bool
        +logout() void
        +view_user_info(id) User
        +update_user_info(id, password, name, mobile, email, address) bool
        +remove_user(id) bool
        +list_users() list
    }

    %% ==================== ORDER DOMAIN ====================
    class Item {
        -__item_id : String
        -__title : String
        -__description : String
        -__start_price : int
        -__status : String
        -__seller : String
        +get_item_id() String
        +get_title() String
        +get_description() String
        +get_start_price() int
        +get_status() String
        +get_seller() String
        +set_status(status) void
        +__str__() String
    }
    class ItemDAO {
        -__itemDB : dict
        +insert_item(item) bool
        +select_item_by_id(item_id) Item
        +select_all_items() list
        +update_item(item_id, item) bool
        +delete_item(item_id) bool
    }
    class ItemService {
        +item_id_seq : int
        -__dao : ItemDAO
        +register_item(title, start_price, description, seller) bool
        +get_all_items() list
        +get_item(item_id) Item
        +cancel_auction(item_id) bool
    }

    %% ==================== BID DOMAIN ====================
    class Bid {
        -__bid_id : int
        -__item_id : String
        -__user_id : String
        -__bid_amount : int
        +get_bid_id() int
        +get_item_id() String
        +get_user_id() String
        +get_bid_amount() int
        +__str__() String
    }
    class BidDAO {
        -__bidDB : dict
        +insert_bid(bid) bool
        +select_all_bids() list
        +delete_bid(bid_id) bool
    }
    class BidService {
        +bid_id_seq : int
        -__dao : BidDAO
        +place_bid(item_id, user_id, bid_amount, item_service) bool
        +get_user_bids(user_id) list
        +get_item_bids_sorted(item_id) list
        +cancel_bid(bid_id) bool
    }

    %% ==================== WIN DOMAIN ====================
    class Winning {
        -__win_id : String
        -__item_id : String
        -__user_id : String
        -__final_amount : int
        -__status : String
        +get_win_id() String
        +get_item_id() String
        +get_user_id() String
        +get_final_amount() int
        +get_status() String
        +set_status(status) void
        +__str__() String
    }
    class WinningDAO {
        -__winningDB : dict
        +insert_winning(winning) bool
        +select_all_winnings() list
        +select_winning(win_id) Winning
        +delete_winning(win_id) bool
    }
    class WinningService {
        +win_id_seq : int
        -__dao : WinningDAO
        +close_auction_and_select_winner(item_id, bid_service, item_service) bool
        +get_user_winnings(user_id) list
        +get_all_winnings() list
        +cancel_winning(win_id, item_service) bool
    }

    %% ==================== INQUIRY DOMAIN ====================
    class Inquiry {
        -__inquiry_id : String
        -__user_id : String
        -__title : String
        -__content : String
        -__answer : String
        -__status : String
        +get_inquiry_id() String
        +get_user_id() String
        +get_title() String
        +get_content() String
        +get_answer() String
        +get_status() String
        +set_title(title) void
        +set_content(content) void
        +set_answer(answer) void
        +set_status(status) void
        +__str__() String
    }
    class InquiryDAO {
        -__inquiryDB : dict
        +insert_inquiry(inquiry) bool
        +select_all_inquiries() list
        +select_inquiry(inquiry_id) Inquiry
        +update_inquiry(inquiry_id, inquiry) bool
    }
    class InquiryService {
        +inquiry_id_seq : int
        -__dao : InquiryDAO
        +register_inquiry(user_id, title, content) bool
        +get_user_inquiries(user_id) list
        +get_all_inquiries() list
        +update_inquiry(inquiry_id, user_id, title, content) bool
        +answer_inquiry(inquiry_id, answer_text) bool
    }

%% ==================== RELATIONSHIPS ====================
    ConsoleMarket --> UserService
    ConsoleMarket --> ItemService
    ConsoleMarket --> BidService
    ConsoleMarket --> WinningService
    ConsoleMarket --> InquiryService

    UserService --> UserDAO
    ItemService --> ItemDAO
    BidService --> BidDAO
    WinningService --> WinningDAO
    InquiryService --> InquiryDAO

    UserDAO "1" *-- "many" User
    ItemDAO "1" *-- "many" Item
    BidDAO "1" *-- "many" Bid
    WinningDAO "1" *-- "many" Winning
    InquiryDAO "1" *-- "many" Inquiry
