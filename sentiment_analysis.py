from textblob import TextBlob

def analyze_sentiment(feedback):
    blob = TextBlob(feedback)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.1:
        label = "Positive"
        emoji = "😊"
    elif polarity < -0.1:
        label = "Negative"
        emoji = "😞"
    else:
        label = "Neutral"
        emoji = "😐"

    return {
        "feedback": feedback,
        "label": label,
        "emoji": emoji,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3)
    }


def display_result(result):
    print("\n" + "=" * 55)
    print(f"  Feedback    : {result['feedback']}")
    print(f"  Sentiment   : {result['emoji']}  {result['label']}")
    print(f"  Polarity    : {result['polarity']}")
    print(f"  Subjectivity: {result['subjectivity']}")
    print("=" * 55)


def analyze_multiple(feedbacks):
    counts = {"Positive": 0, "Neutral": 0, "Negative": 0}
    for fb in feedbacks:
        result = analyze_sentiment(fb)
        display_result(result)
        counts[result["label"]] += 1

    print("\nSUMMARY:")
    print(f"  😊 Positive : {counts['Positive']}")
    print(f"  😐 Neutral  : {counts['Neutral']}")
    print(f"  😞 Negative : {counts['Negative']}")
    print(f"  Total       : {sum(counts.values())}")


def interactive_mode():
    print("\n" + "=" * 55)
    print("   SENTIMENT ANALYSIS  (type 'quit' to exit)")
    print("=" * 55)

    while True:
        feedback = input("\n Enter customer feedback: ").strip()

        if feedback.lower() in ["quit", "exit", "q"]:
            print("\n Goodbye!")
            break

        if not feedback:
            print(" Please enter some text.")
            continue

        result = analyze_sentiment(feedback)
        display_result(result)


if __name__ == "__main__":
    sample_feedbacks = [
        "I absolutely love this product! It is amazing and works perfectly.",
        "The delivery was okay, nothing special about it.",
        "Terrible experience! The item was broken and customer service was rude.",
        "Great quality and very fast shipping. Highly recommend!",
        "Not bad, but could be better. Average product for the price.",
        "Worst purchase ever. Complete waste of money. Very disappointed."
    ]

    analyze_multiple(sample_feedbacks)
    interactive_mode()
