def output_ratings():

    open_file = open("scores.txt")
    rest_dict = {}

    for line in open_file:
        line = line.rstrip()
        entries = line.split(":")
        # print entries

        rest_dict[entries[0]] = entries[1]

    sorted_keys = sorted(rest_dict.keys())
    for word in sorted_keys:
        print "Restaurant '%s' is rated at %s" % (word, rest_dict[word])


output_ratings()