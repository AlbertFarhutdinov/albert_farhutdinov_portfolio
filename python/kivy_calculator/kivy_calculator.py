from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    operators = ['/', '*', '+', '-']
    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['.', '0', 'C', '+'],
    ]
    last_button_was_operator = None
    last_button = None
    solution = TextInput(
        multiline=False, readonly=True, halign='right', font_size=55
    )

    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.solution)
        for row in self.buttons:
            row_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                )
                button.bind(on_press=self.on_button_press)
                row_layout.add_widget(button)
            main_layout.add_widget(row_layout)

        equals_button = Button(
            text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ''
        else:
            # For pressing two operators in a row
            if current and (self.last_button_was_operator and (button_text in self.operators)):
                return
            # If the first character is an operator
            elif current == '' and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_button_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == '__main__':
    app = MainApp()
    app.run()