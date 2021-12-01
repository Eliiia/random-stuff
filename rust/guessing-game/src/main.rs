use std::io;

fn main() {
    println!("Hey, welcome!");
    println!("Input your guess :)");

    let mut guess = String::new(); // `mut` allows the variable to be edited later
                                   // `::new()` is the function that creates the new thing

    io::stdin() // could also use `std::io::stdin()`, but this is nicer, obviously
        .read_line(&mut guess) // says to save the output to the mutable variable `guess`
        .expect("Failed to read line"); // on an error, says this then quits

    println!("You guessed: {}", guess)
}
