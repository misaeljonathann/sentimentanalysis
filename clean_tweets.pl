use strict;
use warnings;

my $filename = 'tweets.txt';

my $fileout = "tweets_cleaned.txt";

open(my $fh, '<:encoding(UTF-8)', $filename)
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
	$line =~ s/[\s]{2,}/ /g; #remove double whitespace
	$line =~ s/\\n/ /g; #remove \n

	print $output $line . "\n";
	
}	