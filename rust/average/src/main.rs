use std::io;

fn main() {
    let mut numbers: Vec<f32> = Vec::new();

    loop {
        println!("Input a number, or 'quit':");

        let mut inp = String::new();

        io::stdin()
            .read_line(&mut inp)
            .expect("Failed to read line");

        if inp == "quit\n" {
            break;
        };

        let inp: f32 = match inp.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        numbers.push(inp);
    }

    // average:
    let mut total: f32 = 0.0;
    for x in &numbers {
        total += x;
    }

    let average = total / numbers.len() as f32;
    println!("Average: {}", average);
}
