import sys
import time

def print_lyrics():
    lyrics = [
        ("Ooh-ooh, ooh", 1.2),
        ("Ooh-ooh, ooh", 1.2),
        ("Mm-mm, mm", 1.5),
        ("Mm-mhm, mm", 1.5),
        ("It's just another night", 1.5),
        ("Just another fight for my life", 1.5),
        ("It’s alright, because everything dies", 1.5),
        ("Nobody know why", 1.6),
        ("Wetin I go do?", 1.4),
        ("Wetin you go do", 1.4),
        ("When you feelin' like you fallin'", 1.5),
        ("And you can’t find nothing to hold on to?", 1.8),
        ("Memories, uh-oh, carry me, go", 1.5),
        ("Carry me, go, oh-na, yeah", 1.5),
        ("Sick and tired of it all, take me far away", 1.6),
        ("Mr DJ, gbemi trabaye", 1.4),
        ("Now man no fit trust anybody", 1.3),
        ("Na hin make I no fit shout", 1.5),
        ("My body don dey tire, eh", 1.4),
        ("E make me madder, eh", 1.4),
        ("My head don scatter, eh", 1.4),
        ("My holy father, eh", 1.4),
        ("My body don dey tire, eh", 1.4),
        ("E make me madder, eh", 1.4),
        ("When my whole world is set on fire", 1.6),
        ("Don't leave me alone", 2.0)
    ]
    
    def type_text(text, speed=0.07):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()  # Newline after each lyric
    
    for text, delay in lyrics:
        type_text(text, speed=0.07)  # Typing effect
        time.sleep(delay)  # Delay based on your timing

if __name__ == "__main__":
    print_lyrics()
