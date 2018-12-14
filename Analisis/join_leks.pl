#UNTUK CLEAN DIKIT BAGIAN POSITIVE DAN NEGATIVE WORDS

use strict;
use warnings;



# #IF YOU WANT TO SET FILE MANUALLY, UNCOMENT THIS PART
my $filein = "negative_words2.txt";
my $filein2 = "negatif.txt";

my $fileout = "negative_gabung.txt";


open(my $fh, '<:encoding(UTF-8)', $filein)
  or die "File tidak bisa dibuka";

open(my $fh2, '<:encoding(UTF-8)', $filein2)
  or die "File tidak bisa dibuka";

open(my $output, '>', $fileout) or die $!;

my @words_list;

#Membaca file KourpusD perbaris 
while (my $row = <$fh>) {
	chomp $row;
	push @words_list, $row;
}	

while (my $row = <$fh2>) {
	chomp $row;
	push @words_list, $row;
}	

sub uniq {
    my %seen;
    grep !$seen{$_}++, @_;
}

my @res = uniq(@words_list);
my @sorted_words = sort { lc($a) cmp lc($b) } @res;

foreach my $w (@sorted_words) {
	print $output $w . "\n";
}

