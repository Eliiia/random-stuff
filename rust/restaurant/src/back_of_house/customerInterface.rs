pub struct Breakfast {
    pub toast: String,      // you can select the type of toast from outside, but
    seasonal_fruit: String, // the seasonal fruit, you cannot
    // the seasonal fruit must be selected in the impl below
    pub appetizer: Appetizer, // made public so that the appetizer can be changed after
}

impl Breakfast {
    // public because the struct Breakfast is public
    pub fn summer(toast: &str, appetizer: Appetizer) -> Breakfast {
        Breakfast {
            toast: String::from(toast),
            seasonal_fruit: String::from("peaches"),
            appetizer,
        }
    }
}

pub enum Appetizer {
    Soup,
    Salad,
}
