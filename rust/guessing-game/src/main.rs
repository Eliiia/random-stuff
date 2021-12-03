use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Hey, welcome!");

    let secret = rand::thread_rng().gen_range(1..101); // start is inclusive, end is exclusive.
        // can also replace with 1..=100 to make end inclusive
        // thread_rng() creates a new thing for generating numbers

    loop { 
        println!("Input your guess :) (secret number is {})", secret);

        let mut guess = String::new(); // `mut` allows the variable to be edited later
            // `::new()` is the function that creates the new thing

        io::stdin() // could also use `std::io::stdin()`, but this is nicer, obviously
            .read_line(&mut guess) // says to save the output to the mutable variable `guess`
            .expect("Failed to read line"); // on an error, says this then quits

        //let guess: u32 = guess.trim().parse().expect("Please type a number!"); // shadowing; equivalent to guess = guess.trim().parse() etc
            // `: u32` specifies the type of it is an unsigned 32 bit integer. usually not necessary
            // expect() also crashes the program with that string, if there is an error

        let guess: u32 = match guess.trim().parse() { // parse returns a Result type, which we can check the content of:
            // `match` is used similarly to a switch statement, in a way
            Ok(num) => num, // if it results in an Ok, pass the number back
            Err(_) => continue, // if it results in an error, continue the loop
        };

        println!("You guessed");
        //println!("Answer is {}", secret)

        match guess.cmp(&secret) { 
            // by using secret here, it's suggested to the compiler that it should be the same type as guess - u32
            Ordering::Less => println!("Too small :("),
            Ordering::Greater => println!("Too big :("),
            Ordering::Equal => {
                println!("You win!!!! c:");
                break;
            },
        }
    }
}
