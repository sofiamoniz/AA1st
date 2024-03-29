from LCS_memoization_wrapper import LCS_memoization_wrapper
from LCS_memoization import LCS_memoization


def main():
    string1 = '''ACT I

            SCENE I. Elsinore. A platform before the Castle.

            Enter Francisco and Barnardo, two sentinels.

            BARNARDO. Who’s there?

            FRANCISCO. Nay, answer me. Stand and unfold yourself.

            BARNARDO. Long live the King!

            FRANCISCO. Barnardo?

            BARNARDO. He.

            FRANCISCO. You come most carefully upon your hour.

            BARNARDO. ’Tis now struck twelve. Get thee to bed, Francisco.

            FRANCISCO. For this relief much thanks. ’Tis bitter cold, And I am sick
            at heart.

            BARNARDO. Have you had quiet guard?

            FRANCISCO. Not a mouse stirring.

            BARNARDO. Well, good night. If you do meet Horatio and Marcellus, The
            rivals of my watch, bid them make haste.

            Enter Horatio and Marcellus.

            FRANCISCO. I think I hear them. Stand, ho! Who is there? '''

    string2 = ''' MARCELLUS. Holla, Barnardo!

                BARNARDO. Say, what, is Horatio there?

                HORATIO. A piece of him.

                BARNARDO. Welcome, Horatio. Welcome, good Marcellus.

                MARCELLUS. What, has this thing appear’d again tonight?

                BARNARDO. I have seen nothing.

                MARCELLUS. Horatio says ’tis but our fantasy, And will not let belief
                take hold of him Touching this dreaded sight, twice seen of us.
                Therefore I have entreated him along With us to watch the minutes of
                this night, That if again this apparition come He may approve our eyes
                and speak to it.

                HORATIO. Tush, tush, ’twill not appear.

                BARNARDO. Sit down awhile, And let us once again assail your ears, That
                are so fortified against our story, What we two nights have seen.

                HORATIO. Well, sit we down, And let us hear Barnardo speak of this.
                '''
    #lcs = LCS_memoization(string1,string2)
    #lcs.get_lcs_len_memoization()
    
    lcs = LCS_memoization_wrapper("ABAABA", "ACBAALKB")
    lcs.get_lcs_len_memoization()

if __name__ == '__main__':
    main()
