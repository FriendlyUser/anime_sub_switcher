import argparse

def get_video_length(video_file):
    import subprocess
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', video_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout.decode('utf-8'))

# compare lengths

def compare_lengths(video1, video2):
    length1 = get_video_length(video1)
    length2 = get_video_length(video2)
    return length1 / length2

def diff_lengths(video1, video2):
    length1 = get_video_length(video1)
    length2 = get_video_length(video2)
    return length1 - length2
if __name__ == '__main__':
    # take two video inputs
    parser = argparse.ArgumentParser()
    parser.add_argument('video1', type=str)
    parser.add_argument('video2', type=str)
    args = parser.parse_args()
    video1 = args.video1
    video2 = args.video2
    number = compare_lengths(video1, video2)
    print(number)
    if number > 1:
        print(f'{video1} is {number} times faster than {video2}')
    else:
        print(f'{video2} is {1/number} times faster than {video1}')

    video_len_diff = diff_lengths(video1, video2)
    print(f'Length difference: {video_len_diff} seconds')
