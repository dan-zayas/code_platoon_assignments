-- GRUBHUB
CREATE TABLE Restaurants(
    id SERIAL PRIMARY KEY,
    restaurant_name string,
    cuisine string,
    price string,
    avg_rating int
);

CREATE TABLE MenuItems(
    id SERIAL PRIMARY KEY,
    restaurant string REFERENCES Restaurants(id),
    blue_id REFERENCES BAUSers(id),
    dish string,
    price int,
    sale_price int
);

-- SHARED TRANSACTIONS
CREATE TABLE Orders(
    id SERIAL PRIMARY KEY,
    ordered_by REFERENCES Users(id),
    order_number int,
    menu_item_list REFERENCES MenuItems(id),
    quantity int NOT NULL
);

CREATE TABLE Followups(
    id SERIAL PRIMARY KEY,
    order_id REFERENCES Orders(order_number),
    delivery_rating int,
    restaurant_rating int
);

CREATE TABLE Promotions(
    id SERIAL PRIMARY KEY,
    discount int,
    region REFERENCES Addresses(zip_code)
);

-- BLUE APRON
CREATE TABLE BAUsers(
    id SERIAL PRIMARY KEY,
    bh_id REFERENCES Users(id)
);

CREATE TABLE ServicePlans(
    id SERIAL PRIMARY KEY,
    dietary_restriction string,
    frequency int
);

CREATE TABLE Recipes(
    id SERIAL PRIMARY KEY,
    dish string,
    ingredients string
)

-- SHARED DATA
CREATE TABLE Users(
    id SERIAL PRIMARY KEY,
    restaurant_owned string REFERENCES Restaurants(id),
    first_name string,
    last_name string,
    email string,
    "password" string
);

CREATE TABLE Addresses(
    id SERIAL PRIMARY KEY,
    user_id integer REFERENCES Users(id),
    business_id integer REFERENCES Restaurants(id),
    street string,
    street2 string,
    city string,
    "state" string,
    zip_code string,
    country string,
    phone string
);

