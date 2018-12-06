use strict;
use warnings;

my $filename = 'user_susipudjiastuti.txt';

my $fileout = "unik_susipudjiastuti.txt";

open(my $fh, '<:encoding(UTF-8)', $filename)
  or die "File tidak bisa dibuka";

open(my $output, '>', $fileout) or die $!;

my %dictionary;

#Membaca file KourpusD perbaris 
while (my $row = <$fh>) {
	chomp $row;
	my $line = lc($row);
	$line  =~ s/^.*=> b//g;
	$line = substr($line,1,length($line)-2);
	$line  =~ s/rt @[\S]+//g; #remove rt @blablabla (retweet)
	$line  =~ s/@[\S]+//g; #remove @blabla (mention)
	$line  =~ s/https:[\S]+//g; #remove link
	$line  =~ s/[\S]*\\[\S]*//g; #remove undefined string \x2\x80 
	$line =~ s/[[:punct:]][\s]/ /g; #remove unrelated punct
	$line =~ s/[\s][[:punct:]]/ /g; #remove unrelated punct
	$line =~ s/[\s]{2,}/ /g; #remove double whitespace

	my @words = split(' ', $row);

	#iterasi semua token perbaris, filter token, hapus punctuation di depan dan di belakang dan cek apakah itu kata
	foreach my $word (@words) {
		#hapus semua punctuation pada akhir token
		while ($word =~ /[[:punct:]]+$/){
			$word = substr($word,0,-1);
		}

		#hapus semua punctuation pada awal token
		while ($word =~ /^[[:punct:]]+/){
			$word = substr($word,1,length($word));
		}

		#Cek apakah token tersebut memenuhi kiteria kata atau tidak
		if (($word =~ /^[A-Za-z]+[-']?[A-Za-z]+$/) || ($word =~ /^[A-Za-z]+$/)){
			if ($dictionary{lc($word)}) {
					$dictionary{lc($word)} += 1;
				} 
				else {
					$dictionary{lc($word)} = 1;
				}
		}
	}
}	

my $number = 1;
foreach my $str (sort {$a cmp $b} keys %dictionary) {
	printf $output "%s\t%s\n", $number, $str;
	$number++;
    
}