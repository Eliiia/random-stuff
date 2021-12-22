// more examples at:
  // https://www.gtk.org/docs/language-bindings/rust/ <-- different example
  // https://gtk-rs.org/gtk4-rs/stable/latest/docs/gtk4/ <-- this example

use gtk;
use gtk::prelude::*;
use gtk::{Application, ApplicationWindow, Button};

fn main() {
    let application = Application::builder()
        .application_id("com.example.FirstGtkApp")
        .build();

    application.connect_activate(|app| {
        let window = ApplicationWindow::builder()
            .application(app)
            .title("First GTK Program")
            .default_width(350)
            .default_height(70)
            .build();

        let button = Button::with_label("Click me!");
        button.connect_clicked(|_| {
            eprintln!("Clicked!");
        });
        window.set_child(Some(&button));

        window.show();
    });

    application.run();
}