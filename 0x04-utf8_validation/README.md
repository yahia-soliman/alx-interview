# UTF-8
according to [Wikipedia](https://en.wikipedia.org/wiki/UTF-8):
UTF-8 is a **variable-length** **character encoding**, it is the current standard for electronic communication

## The meaning of character encoding
Encoding itself means serializing something into another shape, it might be for encryption, transferring through cables, and so on.

In case of UTF-8, as it is the standard for electronic communication, it deals with character encoding.
We know that computers only understand binary (zeros and ones),
and the wires connecting the internet are also capable of sending only 0 and 1 as signals.
so for you to be able to see this emogi 🤗, and all the letters here and every where
in the internet. What happens is that I wrote this article in a program that can encode this emoji or character into bits (zeros and ones) and same for you,
also your program can decode that stream of bits it got from the internet into the correct shape based on the UTF-8 standard.

If both program didn't accept the same standard, and both machines know the shape of decoded character, the emoji might be ⍰ instead of 🤗.


## The meaning of variable-length
It means that the length of an encoded **code-point** can vary from 1 to 4 bytes

## What are code-points
UTF-8 itself means *Unicode Transformation Format – 8-bit* this means there are other formats for *Unicode Transformation* like `UTF-16` and `UTF-1` and others.

Unicode itself is a standard designed to **unify** the text encoding across the world
and to support all writing systems (Alphabets, Abjads, etc..) that can be used inside computers.

Unicode uses code-points to map each possible character (letter, symbol, emoji, etc..) to a number, and it is capable of containing 1.1 milion characters.

UTF-8 it self is about transforming those number into bits.

In UTF-32 all characters have the same byte length (32 bits is 4 bytes), it is easy just convert the hexadecimal Unicode code-point to binary and you are ok.

But there are downsides in the UTF-32 method:
- it is not compatible with ASCII
- it consumes a lot of space, some characters just need 1 byte (all ASCII)

UTF-8 solves those problems by having a variable byte-length based on the binary represintation of the code-point of the character you need to encode, this means the first 127 code-points in the Unicode (which refers to the whole ASCII) will be only 1 byte of length after encoding it with the UTF-8 method. This means all the ASCII encoded text is a valid UTF-8 encoded text


## How programs encode and decode a character
Lets transform "A", "أ", "鈮" and "🤗"

#### First you need to know the Unicode's code-point of that character

|character|code-point|What is this                          |
|---------|----------|--------------------------------------|
|   A     |  U+0041  |  The first letter of Alphabets       |
|   أ     |  U+0672  |  The first letter of Abjads (arabic) |
|   ₿     |  U+20BF  |  Bitcoin symbol                      |
|   🤗    |  U+1F917 |  Hugging face emoji                  |


If any of these is not appearing properly, search for the code-point followed by "Unicode", it means your machine does not know the shape of this character and you might need to install a font library that has this character


#### Second convert the code-point to bits
The code-point is a number represented in hexa decimal, we need to convert it to bits, but in UTF-8 it is not just coverteng the number from hex to binary, this will work in the UTF-32 method.
But with UTF-8 each character will have differen length of bytes (from 1 to 4) based on it's code-point value and each byte will have a prefix that well tell us later how to decode that stream of bytes into characters.

```txt
bytes   range                   utf-8 prefix
1       U+0000  -> U+007F       0xxxxxxx
2       U+0080  -> U+07FF       110xxxxx 10xxxxxx
3       U+0080  -> U+FFFF       1110xxxx 10xxxxxx 10xxxxxx
4       U+10000 -> U+10FFFF     11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```

- The `x` is the placehodler for the binary representation of the character's code-point.
- The actual encoded bytes' prefixes tells us how many bytes the character has
- The utf-8 method is capable of encoding up to `0x10FFFF` (1,114,111 characters)

Back to our characters lets convert them to binary then to the proper utf-8


|character|code-point| Binary                      | Binary + UTF-8 prefix                      | HEX of the utf-8 binary|
|---------|----------|-----------------------------|--------------------------------------------|------------------------|
|   A     |  U+0041  |  `0100 0001`                |  `0100 0001`                               | 0x41                   |
|   أ     |  U+0672  |  `0110 0111 0010`           |  `1101 1001 1011 0010`                     | 0xD9B2                 |
|   ₿     |  U+20BF  |  `0010 0000 1100 1111`      |  `1110 0010 1000 0011 1000 1111`           | 0xE2838F               |
|   🤗    |  U+1F917 |  `0001 1111 1001 0001 0111` |  `1111 0000 1001 1111 1010 0100 1001 0111` | 0xF09FA497             |


Now this Binary with utf-8 method is ready to go through wires to our friends to be decoded in their computer, the decoding process is the invert of the encoding process so we will have the binary numbers and will convert it the the code-point, by knowing its lenght from the start of the byte then extracting the actual binary representation of the character, from teh binary representation we can get the code-point and from the code point we will know the shape of the character, but luckily we don't need to compute all of that because most programs knows how to do it for us, but it is a very good to know how the utf-8 encoding works


## Resources
See the Wikipedia page of any buzz word you are not understanding

[Nice video explaining Unicode](https://www.youtube.com/watch?v=ut74oHojxqo)

[ASCII, Unicode, UTF-8: Explained Simply](https://www.youtube.com/watch?v=DntKZ9xJ1sM)
