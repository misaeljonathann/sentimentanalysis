use strict;
use warnings;


#take file input and output from argv
my ($filein, $fileout) = @ARGV;


#IF YOU WANT TO SET FILE MANUALLY, UNCOMENT THIS PART
$filein = "tweets_jkw_raw.txt";
$fileout = "tweets_cleaned_jkw.txt";

#exception if no input 
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
	$line  =~ s/^.*[0-9]{2}:[0-9]{2}:[0-9]{2}\sb//g;
	$line = substr($line,1,length($line)-2);
	$line  =~ s/rt @[\S]+//g; #remove rt @blablabla (retweet)
	$line  =~ s/@[\S]+//g; #remove @blabla (mention)
	$line  =~ s/https:[\S]+//g; #remove link
	#$line  =~ s/[\S]*\\[\S]*//g; #remove undefined string \x2\x80 
	$line =~ s/[[:punct:]][\s]/ /g; #remove unrelated punct
	$line =~ s/[\s][[:punct:]]/ /g; #remove unrelated punct
	$line =~ s/[[:punct:]]/ /g; #remove all punct
	$line =~ s/[\s]{2,}/ /g; #remove double whitespace
	$line =~ s/\\n/ /g; #remove \n

	print $output $line . "\n";
	
}	