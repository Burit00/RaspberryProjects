import gpiozero
import time


class LCD:

    def __init__(self, rs: int, en: int, d4: int, d5: int, d6: int, d7: int, cols: int = 16, rows: int = 2):
        self._pin_rs = gpiozero.LED(rs)
        self._pin_en = gpiozero.LED(en)
        self._pin_d4 = gpiozero.LED(d4)
        self._pin_d5 = gpiozero.LED(d5)
        self._pin_d6 = gpiozero.LED(d6)
        self._pin_d7 = gpiozero.LED(d7)

        self._cols = cols
        self._rows = rows

        self.COMMAND = False
        self.CHAR = True

        # Commands constants
        self.LCD_LINES = [0x80, 0xC0]

        # Timing constants
        self.E_PULSE = 0.0005
        self.E_DELAY = 0.0005

        self.clear()

    def __del__(self):
        self.print(" \n ")
        time.sleep(2)

    def _enable_command_mode(self):
        self._pin_rs.on()

    def _enable_char_mode(self):
        self._pin_rs.off()

    def clear(self):
        self.byte(0x33, self.COMMAND)
        self.byte(0x32, self.COMMAND)
        self.byte(0x28, self.COMMAND)
        self.byte(0x0C, self.COMMAND)
        self.byte(0x06, self.COMMAND)
        self.byte(0x01, self.COMMAND)

    def print(self, message: str, justify_style: int = 1):
        messages = message.split("\n") # if message.find("\n") != -1 else message

        rows = self._rows
        if len(messages) < self._rows:
            rows = len(messages)

        for rowIndex in range(rows):
            self.byte(self.LCD_LINES[rowIndex], self.COMMAND)
            if justify_style == 1:
                messages[rowIndex] = messages[rowIndex].ljust(self._cols)
            elif justify_style == 2:
                messages[rowIndex] = messages[rowIndex].rjust(self._cols)
            else:
                messages[rowIndex] = messages[rowIndex].center(self._cols)

            for char in messages[rowIndex]:
                self.byte(ord(char))

    def space_between_just(self, *messages: str, width: int = None):
        if width is None:
            width = self._cols

        messages = [*messages]
        chars_len = sum([len(m) for m in messages])

        skip_messages = []
        while chars_len + len(messages) - 1 > width and len(messages) != 0:
            skip_messages.append(messages.pop())

        if len(messages) == 0:
            return "", skip_messages
        if len(messages) == 1:
            return messages[1].center(width), skip_messages

        rest_of_space: int = (width - chars_len)

        space_between_number: int = int(rest_of_space / (len(messages) - 1))
        space_between: str = " " * space_between_number

        additional_space_number: int = rest_of_space % len(messages) if len(messages) > 2 else 0
        msg = ""

        for messageIndex in range(len(messages)):
            message = messages[messageIndex]

            msg += message + (space_between if (len(messages) - messageIndex - 1 > 0) else "")

            if additional_space_number > len(messages) - messageIndex - 1:
                msg += " "

        return msg, skip_messages

    def _apply(self):
        # Toggle 'Enable' pin
        time.sleep(self.E_DELAY)
        self._pin_en.on()
        time.sleep(self.E_PULSE)
        self._pin_en.off()
        time.sleep(self.E_DELAY)

    def _disable_pins(self):
        self._pin_d4.off()
        self._pin_d5.off()
        self._pin_d6.off()
        self._pin_d7.off()

    # Default mode = True set char
    def byte(self, bits, mode=True):

        if mode:
            self._enable_command_mode()
        else:
            self._enable_char_mode()

        self._set_high_bits(bits)
        self._apply()
        self._set_low_bits(bits)
        self._apply()

    def _set_high_bits(self, bits):
        self._disable_pins()

        if bits & 0x10 == 0x10:
            self._pin_d4.on()
        if bits & 0x20 == 0x20:
            self._pin_d5.on()
        if bits & 0x40 == 0x40:
            self._pin_d6.on()
        if bits & 0x80 == 0x80:
            self._pin_d7.on()

    def _set_low_bits(self, bits):
        self._disable_pins()

        if bits & 0x01 == 0x01:
            self._pin_d4.on()
        if bits & 0x02 == 0x02:
            self._pin_d5.on()
        if bits & 0x04 == 0x04:
            self._pin_d6.on()
        if bits & 0x08 == 0x08:
            self._pin_d7.on()





