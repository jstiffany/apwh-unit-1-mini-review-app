## TITLE & INTRO ##

print("-- AP WORLD HISTORY --")
print("UNIT 1-2 PRACTICE TEST\n")
print("This practice test has 5 questions\nand the answers will be shown\nthroughout the quiz.")
print('Before you begin, answer the questions as A/a, B/b, C/c, D/c.\n EX. "A"')

print("\nYour score will be calculated as well.")

## UNIT 1 QUESTIONS ##

score = 0

def quiz1questiononePrompt():
    global score
    print("\n1. What was the main reason for the\nSong Dynasty’s population growth?")

    quiz1questiononeUser = input("\nA. Expansion of territory\nB. Champa rice\nC. Industrialization\nD. Religious reforms\n").lower()

    if quiz1questiononeUser == "b":
        print("\nCorrect. Champa rice was used since it was drought free,\nharvested many times a year, and even caused a population\nspike.")
        score += 1
    else:
        print("\nIncorrect. The correct answer is Champa rice as it was\ndrought free, could be harvested many times a year and\ncaused a population spike in growth.")
    
def quiz1questiontwoPrompt():
    global score
    print("\n2. Which system best describes political organization in medieval Europe?")

    quiz1questiontwoUser = input("\nA. Bureaucracy\nB. Democracy\nC. Feudalism\nD. Theocracy\n").lower()

    if quiz1questiontwoUser == "c":
        print("\nCorrect. Europe used a decenteralized feudal system.")
        score += 1
    else:
        print("\nIncorrect. Europe used a decenteralized feudal\nsystem in which it was hierarchical.")

def quiz1questionthreePrompt():
    global score
    print("\n3. The Seljuk Empire maintained power primarily through:")

    quiz1questionthreeUser = input("\nA. Civil service exams\nB. Trade monopolies\nC. Military strength\nD. Democratic elections\n").lower()

    if quiz1questionthreeUser == "c":
        print("\nCorrect. They expanded by using mobile and calvary-heavy forces.")
        score += 1
    else:
        print("\nIncorrect. The Seljuk Empire used military strength\nto maintain power.")

def quiz1questionfourPrompt():
    global score
    print("\n4. What was a key effect of the House of Wisdom?")

    quiz1questionfourUser = input("\nA. Spread of feudalism\nB. Preservation and translation of knowledge\nC. Creation of civil service exams\nD. Expansion of Christianity\n").lower()

    if quiz1questionfourUser == "b":
        print("\nCorrect. They trasnlated Greek texts into Arabic.")
        score += 1
    else:
        print("\nIncorrect. The answer is perservation and translation of knowledge\n as scholars at the House of Wisdom tranlated texts\nfrom Greek to Arabic.")

def quiz1questionfivePrompt():
    global score
    print("\n5. Which region had the MOST centralized government?")

    quiz1questionfiveUser = input("\nA. Europe\nB. China\nC. South Asia\nD. Americas\n").lower()

    if quiz1questionfiveUser == "b":
        print("\nCorrect. China has the most centeralized government as\nthey used confucanism.")
        score += 1
    else:
        print("\nIncorrect. China has the most centeralized government as\nthey used confucanism.")

unit1quizOrder = [quiz1questiononePrompt, quiz1questiontwoPrompt, quiz1questionthreePrompt, quiz1questionfourPrompt, quiz1questionfivePrompt]

## UNIT 2 QUESTIONS ##

score = 0

def quiz2questiononePrompt():
    global score
    print("\n1. Which of the following best explains why the Indian Ocean trade network expanded more than the Silk Roads?")

    quiz2questiononeUser = input("\nA. It had more government control\nB. It relied on faster and larger-scale transportation\nC. It focused on luxury goods\nD. It avoided cultural interactions\n").lower()

    if quiz2questiononeUser == "b":
        print("\nCorrect. The Indian Ocean network relied on larger-scale\ntransportation due to how large the network was.")
        score += 1
    else:
        print("\nIncorrect. The Indian Ocean network relied on faster and\nlarger-scaled transportation due to the networks size.")

def quiz2questiontwoPrompt():
    global score
    print("\n2. What was a key role of caravanserai along the Silk Roads?")

    quiz2questiontwoUser = input("\nA. They spread Islam into West Africa\nB. They improved maritime navigation\nC. They provided safety and rest for merchants\nD. They taxed trade goods\n").lower()

    if quiz2questiontwoUser == "c":
        print("\nCorrect. Islamic merchants needed spaces to rest during long\ntrips to the Silk Road. The caravanserai enabled this.")
        score += 1

    else:
        print("\nIncorrect. Caravanserais provided saftey and protection for\nmerchants on their way too and from the Silk Road.")

def quiz2questionthreePrompt():
    global score
    print("\n3. Which of the following was a major effect of the Mongol Empire on trade?")

    quiz2questionthreeUser = input("\nA. Decreased trade due to warfare\nB. Isolation of regions\nC. Increased safety and connectivity across Eurasia\nD. Elimination of cultural diffusion\n").lower()

    if quiz2questionthreeUser == "c":
        print("\nCorrect. The Mongol Empires size was big enough to ensure saftey\nwhen it came to traveling.")
        score += 1

    else:
        print("\nIncorrect. The Mongol Empire increased saftey and\nconnectivity across Eurasia.")

def quiz2questionfourPrompt():
    global score
    print("\n4. Which of the following best describes diasporic communities?")

    quiz2questionfourUser = input("\nA. Military groups protecting trade routes\nB. Merchants settling in foreign regions\nC. Government officials collecting taxes\nD. Farmers migrating for agriculture\n").lower()

    if quiz2questionfourUser == "b":
        print("\nCorrect. Merchants traveled into foreign regions for\nmore trade.")
        score += 1

    else:
        print("\nIncorrect. Merchants settled into foreign regions.")

def quiz2questionfivePrompt():
    global score
    print("\n5. The wealth of the Mali Empire was primarily based on:")

    quiz2questionfiveUser = input("\nA. Silk production\nB. Maritime trade\nC. Gold and taxation of trade\nD. Industrial manufacturing\n").lower()

    if quiz2questionfiveUser == "c":
        print("\nCorrect. The Mali Empire used gold and taxation to expand their empire.")
        score += 1

    else:
        print("\nIncorrect. The Mali Empire used gold and taxation to expand their empire.")

unit2quizorder = [quiz2questiononePrompt, quiz2questiontwoPrompt, quiz2questionthreePrompt, quiz2questionfourPrompt, quiz2questionfivePrompt]

## BEGIN ##

while True:
    score = 0
    quizOption = input("Which quiz would you like to begin?(1 or 2) ")

    if quizOption == "1":
        for order in unit1quizOrder:
            order()
        print(f"\nYour final score was a total of: {score}/5.")

    elif quizOption == "2":
        for order in unit2quizorder:
            order()
        print(f"\nYour final score was a total of: {score}/5.")

    else:
        print("\nPlease select 1, 2, or 3.")