use std::io;
use std::collections::HashMap;

fn main() {
    let mut numbers: Vec<u32> = Vec::new();

    loop {
        println!("Input a number, or 'quit':");

        let mut inp = String::new();

        io::stdin()
            .read_line(&mut inp)
            .expect("Failed to read line");

        if inp == "quit\n" {
            break;
        };

        let inp: u32 = match inp.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        numbers.push(inp);
    }

    // average:
    let average = {
        let mut total: u32 = 0;
        for x in &numbers {
            total += x;
        }

        total as f32 / numbers.len() as f32
    };
    println!("Average: {}", average);

    let median = {
        numbers.sort_by(|a, b| a.partial_cmp(b).unwrap()); // do not understand how this works but whatever this is my fault im using f32
        
        numbers[numbers.len()/2]
    };
    println!("Median: {}", median);

    let mode = {
        let mut map = HashMap::new();
        for n in numbers {
            let count = map.entry(n).or_insert(0);
            *count += 1; // .or_insert() returns a reference to the value
        };
        let mut highest = (0,0);
        for x in map {
            if x.1 > highest.1 {
                highest = (x.0, x.1);
            }
        };
        highest.0
    };
    println!("Mode: {:?}", mode);
}
