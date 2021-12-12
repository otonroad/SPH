Private Sub Button1_Click()

Dim VerbEnding As Integer
Dim Conjugation As Integer
Dim Answer As String
Dim Random = New String() {'-o', '-a', '-amos', '-áis', '-an', '-es', '-e', '-emos', '-éis', '-en', '-imos', '-ís', '-en'

Dim IAr As String
IAr = "-o"
Dim YouSAR As String
IAr = "o"
Dim HeAR As String
HeAR = "-a"
Dim WeAR As String
WeAR = "-amos"
Dim YouPLAR As String
YouPLAR = "-áis"
Dim TheyAr As String
TheyAr = "-an"

Dim IEr As String
IEr = "-o"
Dim YouSER As String
YouSER = "-es"
Dim HeER As String
HeER = "-e"
Dim WeER As String
WeER = "-emos"
Dim YouPLER As String
YouPLER = "-éis"
Dim TheyEr As String
TheyEr = "-en"

Dim IIr As String
IIr = "-o"
Dim YouSIR As String
YouSIR = "-es"
Dim HeIR As String
HeIR = "-e"
Dim WeIR As String
WeIR = "-imos"
Dim YouPLIR As String
YouPLIR = "-ís"
Dim TheyIr As String
TheyIr = "-en"

Conjugation = Int((6 * Rnd) + 1)
VerbEnding = Int((3 * Rnd) + 1)


End Sub
