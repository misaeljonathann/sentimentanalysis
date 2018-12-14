#UNTUK CLEAN DIKIT BAGIAN POSITIVE DAN NEGATIVE WORDS

use strict;
use warnings;


#take file input and output from argv
my ($filein, $fileout) = @ARGV;


# #IF YOU WANT TO SET FILE MANUALLY, UNCOMENT THIS PART
$filein = "negative_words.txt";
$fileout = "negative_words2.txt";

# #exception if no input 
if (not defined $filein) {
  die "Need file input\n";
}

if (not defined $fileout) {
  die "Need file output\n";
}


open(my $fh, '<:encoding(UTF-8)', $filein)
  or die "File tidak bisa dibuka";

open(my $output, '>', $fileout) or die $!;

my %dictionary;

#Membaca file KourpusD perbaris 
while (my $row = <$fh>) {
	chomp $row;
	my $line = lc($row);
	$line = substr($line,1,length($line)-3);

	print $output $line . "\n";
}	