struct DialValue<T> {
    id: T,
    stopped_at: u64,
    passed_through: u64,
    next_val: Link<T>,
    prev_val: Link<T>,
}

type Link<T> = Option<Box<DialValue<T>>>;

impl<T> DialValue<T> {
    fn new(item: T) -> Self {
        Self {
            id: item,
            stopped_at: 0,
            passed_through: 0,
            next_val: None,
            prev_val: None,
        }
    }
}

fn main() {}
