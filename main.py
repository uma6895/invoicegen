import speech_recognition as sr
import pyttsx3

class InvoiceGenerator:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        self.items.append({
            'name': name,
            'quantity': quantity,
            'price': price
        })

    def generate_invoice(self):
        total_amount = 0

        print("\n===== Invoice =====")
        print("{:<20} {:<10} {:<10}".format('Item', 'Quantity', 'Amount'))
        print("=" * 40)

        for item in self.items:
            amount = item['quantity'] * item['price']
            total_amount += amount
            print("{:<20} {:<10} {:<10}".format(item['name'], item['quantity'], amount))

        print("=" * 40)
        print("{:<30} {:<10}".format('Total Amount:', total_amount))

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")
            return None

    def speak(self, text):
        print(f"Speaking: {text}")
        self.speaker.say(text)
        self.speaker.runAndWait()

if __name__ == "__main__":
    invoice_gen = InvoiceGenerator()
    assistant = VoiceAssistant()

    # Uncomment the following lines to test voice input and output
    # text_input = assistant.listen()
    # assistant.speak(f"You said: {text_input}")

    # Example code for combining voice input and invoice generation
    assistant.speak("Welcome to the invoice generator. Please state the item name.")
    item_name = assistant.listen()

    if item_name:
        assistant.speak(f"Item name is {item_name}. Please state the quantity.")
        quantity = assistant.listen()

        if quantity:
            assistant.speak(f"Quantity is {quantity}. Please state the price per unit.")
            price_per_unit = assistant.listen()

            if price_per_unit:
                invoice_gen.add_item(item_name, int(quantity), float(price_per_unit))
                invoice_gen.generate_invoice()
                assistant.speak("Invoice generated. Thank you!")
