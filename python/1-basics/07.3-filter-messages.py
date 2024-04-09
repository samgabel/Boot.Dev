# complete filter messages function
# takes list of chat messages and returns 2 lists:

# -----------------------------------------------------------------

def filter_messages(messages):
    complete = []
    metadata = []

    for message in messages:
        words = message.split()

        processed_message = []
        counter = 0

        for word in words:
            if word == "dang":
                counter += 1
            else:
                processed_message.append(word)

        sentence = " ".join(processed_message)

        complete.append(sentence)
        metadata.append(counter)

    print(complete, metadata)
    # return complete, metadata

# -----------------------------------------------------------------

chat_log = [
    "well dang it", 
    "dang the whole dang thing", 
    "kill that knight, dang it",
    "get him!",
    "donkey kong",
    "oh come on, get them",
    "run away from the dang baddies",
]

filter_messages(chat_log)
