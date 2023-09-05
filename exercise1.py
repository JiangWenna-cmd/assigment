def count_and_replace_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    word_to_count = "terrible"
    count = content.count(word_to_count)
    print(f"The word '{word_to_count}' appears {count} times.")

    replacements = {"terrible": ["marvellous", "pathetic"]}
    new_content = content
    for i in range(count):
        new_content=new_content.replace(word_to_count, replacements[word_to_count][i % 2], 1)

    with open("result.txt", 'w') as file:
        file.write(new_content)

count_and_replace_words("file_to_read.txt")

