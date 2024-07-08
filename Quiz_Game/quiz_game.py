import time
import random
from tabulate import tabulate

print("\n=====WELCOME TO QUIZ=====\n")
name=input("First input your name :")
print("------------------------------------------------------------------------------")
print(f"Hello {name},\n")
print("Before we get started, please take a moment to review the rules for the game.")
print("1. Choose only one option at a time.")
print("2. Press 0 if you want to stop the quiz.")
print("3. Do not input an invalid option, as that will terminate the question. " )
print("4. You may skip a question if you need to.")
print("5. Best of Luck!")
print("------------------------------------------------------------------------------")



start=input("Press 'Y' for start the game :").lower()
headers=['S.No.','Question Level','Number of Questions']
data=[
    ['1','Simple ','20'],['2','Medium ','20'],['3','Hard ','20'],['4','Expert ','20']
]


print(tabulate(data,headers,tablefmt='grid'))

level=int(input("Enter level of quiz :"))

print("\n=======================================")
if level==1:
    

    questions=[
        ['Q.What is the capital of France?', 'A) Madrid\t\tB) Berlin\nC) Paris\t\tD) Rome', 'c'], ['Q.Who is the author of the Harry Potter Series?', 'A) J.K.Rowling\t\tB) J.R.R.Tolkein\nC) C.S.Lewis\t\tD) George R.R Martin', 'a'], ['Q.Which scientist is famous for his laws of motion?', 'A) Albert Einstein\t\tB) Galileo Galilei\nC) Isaac Newton\t\tD) Neils Bohr', 'c'], ['Q.What is the capital of Italy?', 'A) Madrid\t\tB) Rome\nC) Lisbon\t\tD) Athens', 'b'], ['Q.What is the primary gas in the Earth atmosphere?', 'A) Oxygen\t\tB) Argon\nC) Carbon Dioxide\tD) Nitrogen', 'd'], ['Q.Which is the smallest continent by land area?', 'A) Europe\t\tB) Australia\nC) Antarctica\t\tD) South America', 'b'], ['Q.Who is known as the Father of Computers?', 'A) Charles Babbage\t\tB) Bill Gates\nC) Alan Turning\t\tD) Steve Jobs', 'a'], ['Q.Which is the fastest land animal?', 'A) Lion\t\tB) Cheeta\nC) Horse\t\tD) Kangaroo', 'b'], ['Q.What is the currency of the United Kingdom?', 'A) Euro\t\tB) Dollar\nC) Pound Sterling\tD) Yen', 'c'], ['Q.Who discovered penicillin?', 'A) Marie Curie\t\tB) Alexander Fleming\nC) Louis Pasteur\t\tD) Joseph Lister', 'b'], ['Q.Which country is known as the land of the rising Sun?', 'A) China\t\tB) Thailand\nC) South Korea\tD) Japan', 'd'], ['Q.Which Planet is known as the Red Planet?', 'A) Earth\t\tB) Mars\nC) Jupiter\t\tD) Venus', 'b'], ['Q.What is the smallest unit of life?', 'A) Cell\t\tB) Atom\nC) Molecule\t\tD) None of these', 'a'], ['Q.Who was the first president of the United States?', 'A) Abraham Lincoln\t\tB) George Washington\nC) Thomas Jefferson\t\tD) John Adams', 'b'], ['Q.Which country is the largest by the land area?', 'A) Canada\t\tB) China\nC) UK\t\tD) Russia', 'd'], ['Q.Who developed the theory of relativity?', 'A) Isaac Newton\t\tB) Nikola Tesla\nC) Albert Einstein\t\tD) None of these', 'c'], ['Q.What is the tallest mountain in the world?', 'A) K2\t\tB) Mount Kilimanjaro\nC) Denali\t\tD) Mount Everest', 'd'], ['Q.Which planet has the most moon?', 'A) Earth\t\tB) Mars\nC) Jupiter\t\tD) Saturn', 'c'], ['Q.Which country is famous for the Eiffel Tower?', 'A) France\t\tB) Italy\nC) Sapin\t\tD) Germany', 'a'], ['Q.What is the square root of 64?', 'A) 6\t\tB) 7\nC) 8\t\tD) 9', 'c'],['Q.What is the powerhouse of the cell?','A) Nucleus\t\tB) Mitrochondria\nC) Ribosome\t\tD) None of these','b'],['Q.What is the tallest building in the world as of 2024?','A) Shanghai Tower\nB) Abraj Al-Bait Clock Tower\nC) Burj Khalifa\nD) One World Trade Center','c']
        ]


        
    questions=random.sample(questions,20)
        
    
if level==2:
    questions=[
        ['Q.What is the official language of Brazil?', 'A) Spanish\t\tB) Portuguese\nC) French\t\tD) English', 'b'], ['Q.Who is known as the Iron Man of India?', 'A) Jawaharlal Nehru\nB) Mahatma Gandhi\nC) Sardar Vallabhbhai Patel\nD) Subas Chandra Bose', 'c'], ['Q.Who is the first women President Of India?', 'A) Indira Gandhi\t\tB) Pratibha Patil\nC) Sarojini Naidu\t\tD) Sushma Swaraj', 'b'], ['Q.What is the capital of Canada?', 'A) Ottawa\t\tB) Toronto\nC) Vancouver\t\tD) Montreal', 'a'], ['Q.In which year was the Battle of Plassey fought?', 'A) 1747\t\tB) 1767\nC) 1234\t\tD) None of these', 'd'], ['Q.What is the longest man-made structure in the world?', 'A) Great Wall of China\t\tB) Panama Canal\nC) Burj Khalifa\t\tD) Hoover Dam', 'a'],['Q.Who won the FIFA World Cup 2022?','A) Brazil\nB) France\nC) Argentina\nD) Germany','c'], ['Q.Which Indian state is known as the "Land of Five Rivers"?', 'A) Haryana\t\tB) Uttar Pradesh\nC) Bihar\t\tD) Punjab', 'd'], ['Q.Who wrote the Indian National Anthem?', 'A) Bankim Chandra Chatterjee\nB) Rabindranath Tagore\nC) Sarojini Naidu\nD) Mahatma Gandhi', 'b'], ['Q.The first battle of Panipat was fought between which of the following?', 'A) Bahur and Lodi\nB) Akbar and Rana Sanga\nC) Humayun and Sher Shah\nD) Aurangzeb and Shivaji', 'a'], ['Q.Who is the "Father of the Indian Constitution"?', 'A) Mahatma Gandhi\t\tB) Jawaharlal Nehru\nC) B.R Ambedkar\t\tD) Sardar Patel', 'c'], ['Q.What is the largest gland in the human body?', 'A) Pancreas\t\tB) Liver\nC) Thyroid\t\tD) Pituitary', 'b'], ['Q.The currency of Bangladesh is:', 'A) Taka\t\tB) Rupee\nC) Dinar\t\tD) Peso', 'a'], ['Q.Who wrote the famous book "Pride and Prejudice"?', 'A) Charles Dickens\t\tB) Jane Austen\nC) Mark Twain\t\tD) Leo Tolstoy', 'b'], ['Q.Who was the first Indian woman to win a Nobel Prize?', 'A) Sarojini Naidu\t\tB) Indira Gandhi\nC) M.S.Subbulakshmi\t\tD) Mother Teresa', 'd'], ['Q.Which Mughal emperor built the Red Fort in Delhi?', 'A) Akbar\t\tB) Jahangir\nC) Shah Jahan\t\tD) Aurangzeb', 'c'], ['Q.Which country is the largest producer of coffee in the world?', 'A) Vietnam\t\tB) Colombia\nC) Indonesia\t\tD) Brazil', 'd'],['Q.Which sport is known as the "King of Sports"?','A) Cricket\t\tB) Basketball\nC) Football\t\tD) Tennis','c'],['Which company recently became the first to reach a $3 trillion market cap?','A) Amazon\t\tB) Microsoft\nC) Apple\t\tD) Google','c'],['Q.What is the name of NASA mission to return humans to the Moon by 2025?','A) Artemis\t\tB) Apollo\nC) Voyager\t\tD) Discovery','a']
        ]

    questions=random.sample(questions,20)
    
if level==3:
    questions=[
        ['Q.Which city is known as the Diamond City of India?', 'A) Mumbai\t\tB) Surat\nC) Jaipur\t\tD) Bangalore', 'b'], ['Q.What is the oldest known civilization in the world?', 'A) Roman\t\tB) Greek\nC) Egyptian\t\tD) Mesopotamian', 'd'], ['Q.Who was the first woman to receive the Nobel Prize in Physics?', 'A) Marie Curie\t\tB) Dorothy Hodgkin\nC) Rosalind Franklin\t\tD) Ada Lovelace', 'a'], ['Q.Which country is known as the Roof Of the World?', 'A) India\t\tB) China\nC) Tibet\t\tD) Nepal', 'c'], ['Q.Which Indian scientist won the Nobel Prize in Physics in 1930?', 'A) Homi J.Bhabha\nB) Vikram Sarabhai\nC) C.V.Raman\nD) Satyendra Nath Bose', 'c'], ['Q.Who is the author of the book "An Era of Darkness"?', 'A) Shashi Tharoor\t\tB) Amartya Sen\nC) Ramchandra Guha\t\tD) Vikram Seth', 'a'], ['Q.The first session of the Indian National Congress was presided over by whom?', 'A) Dadabhai Naoroji\nB) W.C.Bonnerjee\nC) A.O.Hume\nD) Pherozeshah Mehta', 'b'], ['Q.Which among the following is the highest peak in the Western Ghats?', 'A) Anamudi\t\tB) Doddaabetta\nC) Mullayanagiri\t\tD) Agasthyamalai', 'a'], ['Q.The Reserve Bank of India was established in which year?', 'A) 1947\t\tB) 1950\nC) 1955\t\tD) 1935', 'd'], ['Q.Which dynasty built the Khajuraho temples?', 'A) Maurya Dynasty\t\tB) Gupta Dynasty\nC) Chandela Dynasty\t\tD) Chola Dynasty', 'c'], ['Q.Who was the first woman governor of an Indian state?', 'A) Sarojini Naidu\nB) Indira Gandhi\nC) Sucheta Kriplani\nD) Vijayalakshmi Pandit', 'a'], ['Q.In which year did Sikkim become a state of India?', 'A) 1972\t\tB) 1973\nC) 1974\t\tD) 1975', 'd'], ['Q.Which of the following is known as the "Manchester of South India?"?', 'A) Chennai\t\tB) Coimbatore\nC) Bengaluru\t\tD) Hyderabad', 'b'], ['Q.Which is the deepest ocean in the world?', 'A) Java Trench\t\tB) Mariana Trench\nC) Tonga Trench\t\tD) Puerto Rico Trench', 'b'], ['Q.Which of the following countries does not share a border with the Caspian Sea?', 'A) Kazakhstan\t\tB) Turmenistan\nC) Uzbekistan\t\tD) Azerbaijan', 'c'], ['Q.In which year was the Battle of Plassey fought?', 'A) 1757\t\tB) 1747\nC) 1764\t\tD) 1782', 'a'], ['Q.Which of the following is the longest National Highway in India?', 'A) NH 44\t\tB) NH 2\nC) NH 7\t\tD) NH 8', 'a'], ['Q.Which of the following is not a primary greenhouse gas in Earth atmosphere?', 'A)Water Vapour \t\tB) Carbon dioxide\nC) Methane\t\tD) Sulphur Dioxide', 'd'], ['Q.Which Indian state has the largest forest cover in terms of area?', 'A) Madhya Pradesh\t\tB) Arunachal Pradesh\nC) Chhattisgarh\t\tD) Maharashtra', 'a'], ['Q.Which among the following was the first European to encounter the cacao bean\nfrom which chocolate is made?', 'A) Christoper Columbus\t\tB) Hernan Cortes\nC) Vasco da Gama\t\tD) Ferdinand Magellan', 'a'],['Q.Which U.S. president signed the Emancipation Proclamation?','A) George Washington\t\tB) Thomas Jefferson\nC) Abraham Lincoln\t\tD) Andrew Johnson','c'],['Q.Which country recently joined NATO in 2023?','A) Sweden\t\tB) Finland\nC) Ukraine\t\tD) Georgia','b']
        ]   

    
    questions=random.sample(questions,20)
    
if level==4:
    questions=[
        ['Q.Which European country is known as the "Land of Fire and Ice"?','A) Iceland\t\tB) Norway\nC) Finland\t\tD) Sweden','a'],['Q.Who is the author of the novel "One Hundred Years of Solitude"?','A) Mario Vargas Liosa\t\tB) Isabel Allende\nC) Jorge Luis Borges\t\tD) Gabriel Garcia Marquez','d'],['Q.What is the highest peak in Africa?','A) Mount Kenya\t\tB) Mount Kilimanjaro\nC) Mount Elgon\t\tD) Mount Meru','b'],['Q.Which country is the largest producer of olive oil?','A) Greece\t\tB) Italy\nC) Spain\t\tD) Turkey','c'],['Q.Who was the founder of the Maurya Empire in ancient India?','A) Ashoka\t\tB) Chandragupta Maurya\nC) Bindusara\t\tD) Harshavardhana','b'],['Q.In which year did India conduct its first nuclear test?','A) 1968\t\tB) 1974\nC) 1984\t\tD) 1998','b'],['Q.What is the ancient name of the Indian city of Varanasi?','A) Banaras\t\tB) Prayag\nC) Kashi\t\tD) Ayodhya','c'],['Q.Which Indian freedom fighter was popularly known as "Deshbandhu"?','A) Bal Gangadhar Tilak\nB) Chittaranjan Das\nC) Subhas Chandra Bose\nD) Lala Lajpat Rai','b'],['Q.What is the official language of Ethiopia?','A) Amharic\t\tB) Swahili\nC) Hausa\t\tD) Yoruba','a'],['Which country has the highest number of pyramids in the world?','A) Egypt\t\tB) Mexico\nC) Sudan\t\tD) Guatemala','c'],['Q.Which pharmaceutical company developed the first COVID-19 pill?','A) Pfizer\t\tB) Moderna\nC) AstraZeneca\t\tD) Johnson & Jhonson','a'],['Q.Which ancient civilization built the Machu Picchu?','A) Aztec\t\tB) Inca\nC) Maya\t\tD) Olmec','b'],['Q.Who was the first woman to win an Olympic medal?','A) Mary Kom\t\tB) B.P.T.Usha\nC) C.Karnam Malleswari\t\tD) D.Saina Nehwal','c'],['Q.Which Indian state has the highest literacy rate?','A) Kerla\t\tB) Tamil Nadu\nC) Goa\t\tD) Himachal Pradesh','a'],['Q.Who was the first Indian Governor-General of Independent India?','A) Rajendra Prasad\t\tB) C.Rajagopalachari\nC) Jawaharlal Nehru\t\tD) S.Radhakrishna','b'],['Q.What is the name of the boundary between North and South Korea?','A) 17th Parallel\t\tB) 23rd Parallel\nC) 38th Parallel\t\tD) 45th Parallel','c'],['Q.Who os known as the "Father of modern chemistry"?','A) Antonie Lavoisier\t\tB) Dmitri Mendeleev\nC) Robert Boyle\t\tD) Marie Curie','a'],['Q.What is the longest bone in the human body?','A) Humerus\t\tB) Tibia\nC) Radius\t\tD) Femur','d'],['Q.Which country has the most time zones?','A) Russia\t\tB) US\nC) Canada\t\tD) France','d'],['Which film won Oscar for Best Picture in 2020?','A) 1917\t\tB) Joker\nC) Parasite\t\tD) Once Upon a Time In Hollywood','c'],['Q.Who won the 2024 Golden Globe for Best Actor?','A) Will Smith\nB) Leonardo DiCaprio\nC) Brad Pitt\nD) Joaquin Phoenix','b'],['Q.Which book series has recently been adapted into a hit television series in 2024?','A) The Wheel of Time\nB) A song of ice and fire\nC) The Witcher\nD)Percy Jackson','d']
        ]
    questions=random.sample(questions,20)

correct=0
incorrect=0
skip=0
invalid=0
f=1
if start=="y":
    for i in range(len(questions)):
        print(questions[i][0])
        print(questions[i][1])
        option=input("Enter Answer :").lower()
        if option==questions[i][2]:
            correct+=1
            print("Correct Answer")
        elif option=='':
            skip+=1
            print("You skip the question")
        elif option=='0':
            f=0
            break
        elif option not in 'abcd':
            print("Warning!\nInvalid Input...")
            invalid+=1
        else:
            print("Incorrect Answer")
            incorrect+=1
    
        time.sleep(0.7)
        print("\033[2J\033[H")
    
    

    print("=============================")
    if level==1:
        print("Questions Level  : Easy")
    elif level==2:
        print("Questions Level  : Medium")
    elif level==3:
        print("Questions Level  : Hard")
    else:
        print("Questions Level  : Expert")
    print(f"Total Questions  : {len(questions)}")
    print(f"Attempted        : {correct+incorrect+skip}")
    print(f"Not Attempted    : {len(questions)-(correct+incorrect+skip)}")
    print("=============================")
    print(f"Correct Answer   : {correct}")
    print(f"Incorrect Answer : {incorrect}")
    print(f"Skip Answer      : {skip}")
    print(f"Terminate Answer : {invalid}")
    print('\n')
    print("=============================")
    print("=======Thanks for Quiz=======")
else:
    print("=====Thanks=====")


