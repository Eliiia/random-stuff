// import a file
mod back_of_house; // next line would crash without this

pub use crate::back_of_house::customerInterface as order;

pub fn eat_at_restaurant() {
    // order meal:
    let mut meal = order::Breakfast::summer("Rye", order::Appetizer::Salad);
    // change bread afterwards:
    meal.toast = String::from("Wheat");

    println!("I'd like {} toast please!", meal.toast);

    // the below wont compile, as seasonal_fruit is not public
    //meal.seasonal_fruit = String::from("blueberries")
}
