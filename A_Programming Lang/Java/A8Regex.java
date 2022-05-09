/*
 Regular Expression :-
  - Special sequence of characters that helps to match or find other strings or sets of string, Using specialized 
    syntax held in pattern
  - java.util.regex package used

  Pattern Class :-
   - To create pattern first invoke one of its public static compile() method, which will then return Pattern object
   - Method accept regular expression as first argument

  Matcher Class :−    
   - Matcher object is the engine that interprets pattern and performs match operations against input string
   - Matcher defines no public constructors
   - Obtain Matcher object by invoking matcher() method on Pattern object

  PatternSyntaxException :− 
   - PatternSyntaxException object is unchecked exception that indicates syntax error in regular expression pattern

  Capturing Group :-
   - Way to treat multiple characters as a single unit
   - To find out how many groups are present in expression, call groupCount method on matcher object

  Common use Symbols :-
    ^	    Match beginning of line
    $	    Match end of line
    .	    Match single character except newline, Using m option allows it to match newline as well
    [...]	Match any single character in brackets
    [^...]	Match any single character not in brackets
    \A	    Beginning of entire string
    \z	    End of entire string
    a| b	Match either a or b
    \W	    Match nonword characters
    \w	    Match word characters
    \s	    Match whitespace, Equivalent to [\t\n\r\f]
    \S	    Match nonwhitespace
    \d	    Match digits. Equivalent to [0-9].
    \D	    Match nondigits


  Method :-
   Start   :- Return start index of previous match
   End     :- Return offset after last character matched
   find    :- Attempt to find next subsequence of input sequence that matches pattern
   matches :- Attempt to match entire region against pattern
   lookingAt :- match input sequence starting at beginning of the region against pattern

  Replacements Methods :-
   replaceAll         :- Replace every subsequence of input sequence
   replaceFirst       :- Replace first subsequence of input sequence
   quoteReplacement   :- Return literal of replacement string or specified string
   Matcher appendReplacement :- Implement non-terminal append-and-replace step
   StringBuffer appendTail   :- terminal

  PatternSyntaxException Class Methods :-
   getIndex       :- Return error index
   getPattern     :- Retrieve erroneous regular expression pattern
   getMessage     :- Return multi-line string containing error
   getDescription :- Return description error message

*/