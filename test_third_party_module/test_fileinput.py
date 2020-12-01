import fileinput


# with fileinput.input() as f_input:
#     for line in f_input:
#         print(line, end='')


with fileinput.input('abc.txt') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')


# abc.txt 1 German Unity Day
# abc.txt 2 From Wikipedia, the free encyclopedia
# abc.txt 3 The Day of German Unity (German: Tag der DeutschenEinheit) is the national day
# abc.txt 4 of Germany, celebrated on 3 October as a public holiday.
# abc.txt 5 It commemorates the anniversary of German reunification in 1990,
# abc.txt 6 when the goal of a united Germany that originated in the middle of the
# abc.txt 7 19th century, was fulfilled again.
# abc.txt 8 Therefore, the name addresses neither the re-union nor the union, but the unity of Germany.
# abc.txt 9 The Day of German Unity on 3 October has been the German national holiday since 1990,
# abc.txt 10 when the reunification was formally completed.
