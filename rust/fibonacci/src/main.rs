fn main() {
    const L: usize = 20; // length

    let mut arr = vec![0, 1];
    // alternate method of vectoring:
    /*let mut arr: Vec<u32> = Vec::new();
    arr.push(0);
    arr.push(1);*/

    for x in 2..L {
        arr.push(arr[x - 1] + arr[x - 2])
    }

    for x in arr {
        println!("{}", x)
    }
}
