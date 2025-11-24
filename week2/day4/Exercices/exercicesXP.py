# #Exercice 1
import random
import sys
def get_words_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def get_random_sentence(sentence_length, file_path="words.txt"):
    words = get_words_from_file(file_path)
    if not words:
        print("Error: The word list is empty.")
        sys.exit(1)
    
    selected_words = [random.choice(words) for _ in range(sentence_length)]
    sentence = " ".join(selected_words).lower()
    return sentence

def main():
    print("Welcome to the Random Sentence Generator!")
    
    try:
        length = int(input("Enter the desired sentence length (2-20): "))
        if length < 2 or length > 20:
            print("Error: Sentence length must be between 2 and 20.")
            return
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    
    sentence = get_random_sentence(length)
    print("\nGenerated Sentence:")
    print(sentence)

if __name__ == "__main__":
    main()
# #Exercice 2
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print(f"Employee salary: {salary}")

data["company"]["employee"]["birth_date"] = "1990-05-15"  

output_file = "modified_employee.json"
with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

print(f"Modified JSON saved to '{output_file}'")
