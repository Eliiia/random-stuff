fn main() {
    const L:usize = 20; // length

    let mut arr = [0;L];
    arr[1] = 1;

    for x in 2..L {
        arr[x] = arr[x-1]+arr[x-2];
        //println!("{}", x);
    }

    for x in arr {
        println!("{}", x)
    }
}