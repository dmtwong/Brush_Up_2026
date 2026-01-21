//============================================================================
// Name        : firstNonRepeatChar.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

/*
Problem Description
Given a string A denoting a stream of lowercase alphabets. You have to make new string B.
B is formed such that we have to find first non-repeating character each time a character is inserted to the stream
and append it at the end to B. If no non-repeating character is found then append '#' at the end of B.
Problem Constraints
1 <= length of the string <= 100000
Input Format
The only argument given is string A.
Output Format
Return a string B after processing the stream of lowercase alphabets A.
Example Input
Input 1:
 A = "abadbc"
Input 2:
 A = "abcabc"
Example Output
Output 1:
 "aabbdd"
Output 2:
 "aaabc#"
Example Explanation
Explanation 1:
    "a"      -   first non repeating character 'a'
    "ab"     -   first non repeating character 'a'
    "aba"    -   first non repeating character 'b'
    "abad"   -   first non repeating character 'b'
    "abadb"  -   first non repeating character 'd'
    "abadbc" -   first non repeating character 'd'
Explanation 2:

    "a"      -   first non repeating character 'a'
    "ab"     -   first non repeating character 'a'
    "abc"    -   first non repeating character 'a'
    "abca"   -   first non repeating character 'b'
    "abcab"  -   first non repeating character 'c'
    "abcabc" -   no non repeating character so '#'

*/


#include <iostream>
#include <string>
#include <queue>
#include <vector>
// #include <unordered_map>

using namespace std;

// string Solution::solve(string A) {
string solve(string A) {
    vector<int> freq_table(26, 0);
    queue<char> char_queue;
    string result = "";

    for (char i : A) {
    	freq_table[i - 'a']++;
    	char_queue.push(i);

        while (!char_queue.empty() && freq_table[char_queue.front() - 'a'] > 1) {
        	char_queue.pop();
        }

        if (!char_queue.empty()) {
        	result += char_queue.front();
        } else {
        	result += '#';
        }
    }
    return result;
}

/*
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
*/

/* Editorial
 * class Solution:
    def solve(self, A):
        st = []
        d = {}
        ans = ''
        for i in A:
            if i in d:
                if i in st:
                    st.remove(i)
            else:
                st.append(i)
                d[i] = 0
            if st:
                ans += st[0]
            else:
                ans +='#'
        return ans
 *
 */

/* Scala:
 * import scala.collection.mutable._

class Solution {
  def solve(str: String): String  = {
    if (str.isEmpty) {
      return ""
    }

    val q = Queue[Char]()
    val charsFoundSoFar = Map[Char, Int]()

    val result = for (ch <- str) yield {
      if (charsFoundSoFar.contains(ch)) {
        // more than one occurence of char 'ch'
        charsFoundSoFar(ch) = 2

        // find next non-repeating char
        while (q.nonEmpty && charsFoundSoFar(q.front) > 1) {
          q.dequeue
        }
      } else {
        // first occurence of char 'ch'
        charsFoundSoFar(ch) = 1
        q.enqueue(ch)
      }

      if (q.isEmpty) '#' else q.front
    }

    result.mkString
  }
}
 *
 */

/*GO
func solve(s string )  (string) {
    q := make([]byte, 0, len(s))
  ans := make([]byte, 0, len(s))

  mp := make(map[byte]int)

  for i := 0 ; i < len(s) ; i++ {
    if v, ok := mp[s[i]] ; ok {
      mp[s[i]] = v + 1
    } else {
      mp[s[i]] = 1
      q = append(q, s[i])
    }

    i:=0
    for ; i<len(q) ; i++ {
      if mp[q[i]] <= 1 {
        ans = append(ans, q[i])
        break
      }
    }
    if i==len(q) {
      ans = append(ans, '#')
    }
    q = q[i:]
  }
  return string(ans)
}

 *
 */

/*
from collections import defaultdict, deque
class Solution:
    # @ returns 0
    def default(x): return 0
    # @param A : string
    # @return a strings
    def solve(self, A):
        chars = defaultdict(self.default)
        ans = ''
        q = deque()

        for char in A:
            q.append(char)
            chars[char] += 1
            while len(q) and chars[q[0]] != 1:
                q.popleft()
            ans += ('#' if not len(q) else q[0])

        return ans
  */
