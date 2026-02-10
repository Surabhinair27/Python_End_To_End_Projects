# 🧠 Quiz App CLI Version
# -----------------------------------

from questions import questions   # question bank import


score = 0   # 🎯 score track


# loop through each question
for q in questions:

    print("\n" + q["question"])

    # options print karo
    for i, opt in enumerate(q["options"], 1):
        print(f"{i}. {opt}")

    choice = int(input("Choose option number: "))

    selected = q["options"][choice - 1]

    # check answer
    if selected == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")


print("\n🎉 Final Score:", score, "/", len(questions))
