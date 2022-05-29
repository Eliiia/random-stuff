import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.lang.reflect.Array;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;

import java.awt.GridLayout;

public class main {

    public static void main(String[] args) {

        // JFrame f = new JFrame("Calculator");
        /*
         * JPanel f = new JPanel(new GridLayout(3, 3));
         * f.setSize(250, 350);
         */
        // f.setLocation(300, 200);
        /*
         * final JTextArea textArea = new JTextArea(10, 40);
         * f.getContentPane().add(BorderLayout.CENTER, textArea);
         * final JButton button = new JButton("Click Me");
         * f.getContentPane().add(BorderLayout.SOUTH, button);
         * button.addActionListener(new ActionListener() {
         * 
         * @Override
         * public void actionPerformed(ActionEvent e) {
         * textArea.append("Button was clicked\n");
         * 
         * }
         * });
         */

        /*
         * final JButton button1 = new JButton("1");
         * final JButton button2 = new JButton("2");
         * final JButton button3 = new JButton("3");
         * final JButton button4 = new JButton("4");
         * final JButton button5 = new JButton("5");
         * f.getContentPane().add(BorderLayout.NORTH, button1);
         * f.getContentPane().add(BorderLayout.NORTH, button2);
         * f.getContentPane().add(BorderLayout.NORTH, button3);
         * f.getContentPane().add(BorderLayout.NORTH, button4);
         * f.getContentPane().add(BorderLayout.NORTH, button5);
         */

        /*
         * final JButton button1 = new JButton("1");
         * final JButton button2 = new JButton("2");
         * f.add(button1, button2);
         */

        /*
         * JPanel[][] buttons = new JPanel[3][3];
         * for (int i = 0; buttons.length < 3; i++) {
         * for (int j = 0; buttons[i].length < 3; j++) {
         * buttons[i][j] = new JPanel(new GridLayout(3, 3));
         * 
         * }
         * }
         */

        JPanel f = new JPanel(new GridLayout(4, 3));

        char[] buttons = { '7', '8', '9', '4', '5', '6', '1', '2', '3', '+', '0', '=' };

        for (char buttonText : buttons) {
            f.add(new JButton(buttonText + ""));
        }

        JFrame frame = new JFrame("Calculator");
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.getContentPane().add(f);
        frame.pack();
        frame.setLocationByPlatform(true);

        frame.setVisible(true);

    }
}