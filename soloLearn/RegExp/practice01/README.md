# Basics: Practice Time

Let's take a look at the following regular expression examples:

## Special Symbols in Username

Let's create a regex to validate a proper username, which should be a string that does not contain the following special characters: **! @ # $ % ^ & \***

We will search the given username for any occurrence these symbols, and if a match is found, deny the username.

The regex will look like this:

```js
/[!@#$%^&*]/
```

## Proper Filenames

Similarly, we can build a regex to validate the filename for a text file, having a `.txt` extension. Let's deny filenames containing any of the following symbles as the **end** of the filename: **! ? @ $ % #**

Our regex will match only names that don't end with these symbols:

```js
/[^!?@$%#]\.txt/
```

> Implement the examples above in your favortie programming language and submit them in the comments section below.
