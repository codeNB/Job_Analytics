"""provide deduping tool for results from target_search"""

def dedup_post_urls(file: str, outfile: str = 'cleaned_post_urls.txt'):
    """ file is the file to dedupe
        outfile is the file to output the deduped file
            defaults to 'cleaned_post_urls.txt """

    urls_in = open(file, 'r')
    urls_out = open(outfile, 'w')
    seen = set()
    count = 0

    # add url to outfile if not encountered before
    for line in urls_in:
        if line not in seen:
            print(line, file=urls_out, end='')
            seen.add(line)
        else:
            count += 1

    print("found {0} duplicates".format(count))
    
if __name__ == "__main__":
    dedup_post_urls(file='../spiders/post_urls.txt', outfile='test.txt')