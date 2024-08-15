from django import forms
from .models import UserProfile

# List of top 80 coding languages
CODING_LANGUAGES = [
    ('Python', 'Python'),
    ('JavaScript', 'JavaScript'),
    ('Java', 'Java'),
    ('C#', 'C#'),
    ('C++', 'C++'),
    ('Ruby', 'Ruby'),
    ('PHP', 'PHP'),
    ('Swift', 'Swift'),
    ('Go', 'Go'),
    ('TypeScript', 'TypeScript'),
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('SQL', 'SQL'),
    ('R', 'R'),
    ('Kotlin', 'Kotlin'),
    ('Scala', 'Scala'),
    ('Perl', 'Perl'),
    ('Haskell', 'Haskell'),
    ('Lua', 'Lua'),
    ('Rust', 'Rust'),
    ('MATLAB', 'MATLAB'),
    ('Objective-C', 'Objective-C'),
    ('Groovy', 'Groovy'),
    ('Dart', 'Dart'),
    ('Clojure', 'Clojure'),
    ('Julia', 'Julia'),
    ('Solidity', 'Solidity'),
    ('Shell', 'Shell'),
    ('Tcl', 'Tcl'),
    ('Scheme', 'Scheme'),
    ('VHDL', 'VHDL'),
    ('ActionScript', 'ActionScript'),
    ('Smalltalk', 'Smalltalk'),
    ('Ada', 'Ada'),
    ('Racket', 'Racket'),
    ('Elixir', 'Elixir'),
    ('COBOL', 'COBOL'),
    ('Forth', 'Forth'),
    ('Verilog', 'Verilog'),
    ('Eiffel', 'Eiffel'),
    ('APL', 'APL'),
    ('SML', 'SML'),
    ('D', 'D'),
    ('Objective-Caml', 'Objective-Caml'),
    ('AWK', 'AWK'),
    ('Erlang', 'Erlang'),
    ('Modula-2', 'Modula-2'),
    ('XSL', 'XSL'),
    ('XSLT', 'XSLT'),
    ('Lisp', 'Lisp'),
    ('OpenCOBOL', 'OpenCOBOL'),
    ('XQuery', 'XQuery'),
    ('SDL', 'SDL'),
    ('IDL', 'IDL'),
    ('RPG', 'RPG'),
    ('Ch', 'Ch'),
    ('Nim', 'Nim'),
    ('PL/SQL', 'PL/SQL'),
    ('Verilog', 'Verilog'),
    ('Starlark', 'Starlark'),
    ('ML', 'ML'),
    ('Zsh', 'Zsh'),
    ('Pike', 'Pike'),
    ('Sh', 'Sh'),
    ('Tcl', 'Tcl'),
    ('SystemVerilog', 'SystemVerilog'),
]

class AdditionalInfoForm(forms.Form):
    coding_languages = forms.ChoiceField(
        label='Coding Languages',
        choices=CODING_LANGUAGES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tech_career_interest = forms.CharField(
        label='Tech Career Interest',
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

class EditProfileForm(forms.ModelForm):
    coding_languages = forms.ChoiceField(
        label='Coding Languages',
        choices=CODING_LANGUAGES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tech_career_interest = forms.CharField(
        label='Tech Career Interest',
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})
    )

    class Meta:
        model = UserProfile
        fields = ['coding_languages', 'tech_career_interest']
