import time

def tone(freq, duration):
	pass

def NOTE(freq, duration):
	pass

def delay(duration):
	#time.sleep(duration)
	pass

def stillalive():
	A3 = 220
	As3 = 233
	B3 = 247
	C4 = 262
	Cs4 = 277
	D4 = 294
	Ds4 = 311
	E4 = 330
	F4 = 349
	Fs4 = 370
	G4 = 392
	Gs4 = 415
	A4 = 440
	As4 = 466
	B4 = 494
	# DURATION OF THE NOTES 
	BPM = 240.0    #  you can change this value changing all the others
	Q = 60/BPM #quarter 1/4 
	H = 2*Q #half 2/4
	E = Q/2   #eighth 1/8
	S = Q/4 # sixteenth 1/16
	W = 4*Q # whole 4/4
	SEMIQUAVER = Q/4
	QUAVER = Q/2
	CROTCHET = Q
	MINIM = Q*2
	QUAVER_DOTTED = QUAVER * 3 / 2
	CROTCHET_DOTTED = CROTCHET * 3 / 2
	MINIM_DOTTED = MINIM * 3 / 2

	delay( MINIM )
	NOTE( G4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( E4, QUAVER )
	# bar 2
	NOTE( Fs4, MINIM )
	delay( MINIM )
	# bar 3...
	delay( CROTCHET_DOTTED )
	NOTE( A3, QUAVER )
	NOTE( G4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( E4, CROTCHET )
	# bar ...4...
	NOTE( Fs4, CROTCHET_DOTTED )
	NOTE( D4, CROTCHET )
	NOTE( E4, QUAVER )
	NOTE( A3, E )
	# bar ...5
	delay( QUAVER )
	NOTE( A3, QUAVER )
	# bar 6...
	NOTE( E4, CROTCHET )
	NOTE( Fs4, QUAVER )
	NOTE( G4, CROTCHET_DOTTED )
	NOTE( E4, QUAVER )
	NOTE( Cs4, CROTCHET )
	# bar ...7...
	NOTE( D4, CROTCHET_DOTTED )
	NOTE( E4, CROTCHET )
	NOTE( A3, QUAVER )
	NOTE( A3, CROTCHET )
	# bar ...8
	NOTE( Fs4, E )
	# bar 9
	delay( MINIM )
	NOTE( G4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( E4, QUAVER )
	# bar 10
	NOTE( Fs4, MINIM )
	delay( MINIM )
	# bar 11...
	delay( CROTCHET_DOTTED )
	NOTE( A3, QUAVER )
	NOTE( G4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( E4, CROTCHET_DOTTED )
	# bar ...12...

	NOTE( Fs4, QUAVER )

	NOTE( D4, CROTCHET_DOTTED )

	NOTE( E4, QUAVER )
	NOTE( A3, CROTCHET_DOTTED )
	# bar ...13

	delay( MINIM_DOTTED )
	#/ bar 14...
	NOTE( E4, CROTCHET )
	NOTE( Fs4, QUAVER )
	NOTE( G4, CROTCHET_DOTTED )
	NOTE( E4, QUAVER )
	NOTE( Cs4, CROTCHET_DOTTED )
	# bar ...15
	# set graphic to radiation.
	NOTE( D4, QUAVER )
	NOTE( E4, CROTCHET )
	# set text rate to 1

	NOTE( A3, QUAVER )
	NOTE( D4, QUAVER )
	NOTE( E4, QUAVER )
	# bar 16
	NOTE( F4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( D4, QUAVER )
	NOTE( C4, QUAVER )
	# set graphic to aperture
	delay( CROTCHET )
	NOTE( A3, QUAVER )

	NOTE( As3, QUAVER )
	# bar 17
	NOTE( C4, CROTCHET )
	NOTE( F4, CROTCHET )
	NOTE( E4, QUAVER )
	NOTE( D4, QUAVER )
	NOTE( D4, QUAVER )
	NOTE( C4, QUAVER )
	# bar 18
	NOTE( D4, QUAVER )
	NOTE( C4, QUAVER )
	NOTE( C4, CROTCHET )
	NOTE( C4, CROTCHET )
	NOTE( A3, QUAVER )
	NOTE( As3, QUAVER )

	# bar 19
	NOTE( C4, CROTCHET )
	NOTE( F4, CROTCHET )
	NOTE( G4, QUAVER )
	NOTE( F4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( D4, QUAVER )
	# bar 20
	NOTE( D4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( F4, CROTCHET )
	NOTE( F4, CROTCHET )
	# set graphic to atom

	NOTE( G4, QUAVER )
	NOTE( A4, QUAVER )
	# bar 21
	NOTE( As4, QUAVER )
	NOTE( As4, QUAVER )
	NOTE( A4, CROTCHET )

	NOTE( G4, CROTCHET )
	NOTE( F4, QUAVER )
	NOTE( G4, QUAVER )
	# bar 22
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( G4, CROTCHET )
	# set graphic to aperture
	NOTE( F4, CROTCHET )

	NOTE( D4, QUAVER )
	NOTE( C4, QUAVER )
	# bar 23
	NOTE( D4, QUAVER )
	NOTE( F4, QUAVER )
	NOTE( F4, QUAVER )
	NOTE( E4, CROTCHET )
	NOTE( E4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( Fs4, QUAVER )
	# bar 24
	delay( MINIM )
	 # a few newlines...
	delay( MINIM )
	# bar 25
	delay( MINIM )
	delay( MINIM )
	# bar 26
	delay( MINIM )
	delay( MINIM )
	# bar 27...
	delay( CROTCHET_DOTTED )
	NOTE( A3, QUAVER )
	NOTE( G4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( E4, QUAVER_DOTTED )
	# bar ...28
	NOTE( Fs4,7)
	delay( MINIM )
	# bar 29...
	delay( MINIM )
	NOTE( G4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( E4, CROTCHET_DOTTED )
	# bar ...30...
	NOTE( Fs4, QUAVER )
	NOTE( D4, CROTCHET )

	NOTE( E4, CROTCHET )

	NOTE( A3, CROTCHET_DOTTED )
	# bar ...31
	delay( E )
	# bar 32

	NOTE( E4, CROTCHET )
	NOTE( Fs4, QUAVER )
	NOTE( G4, CROTCHET_DOTTED )
	# broken heart picture
	NOTE( E4, CROTCHET )
	# bar 33...

	NOTE( Cs4, CROTCHET )
	NOTE( D4, QUAVER )
	NOTE( E4, CROTCHET_DOTTED )
	NOTE( A3, QUAVER )
	NOTE( A3, CROTCHET )
	# explosion picture
	# bar ...34
	NOTE( Fs4, MINIM + QUAVER )
	delay( CROTCHET )
	# bar 35
	delay( CROTCHET_DOTTED )
	NOTE( A3, QUAVER )
	NOTE( B4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( G4, QUAVER )
	NOTE( G4, QUAVER )
	# bar 36
	NOTE( A4, CROTCHET )
	delay( MINIM_DOTTED )
	# bar 37...
	delay( CROTCHET_DOTTED )

	NOTE( A3, QUAVER )
	NOTE( B4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( G4, QUAVER )
	NOTE( G4, CROTCHET_DOTTED )
	# bar ...38...

	NOTE( A4, QUAVER )
	# fire picture
	NOTE( Fs4, CROTCHET_DOTTED )
	NOTE( G4, QUAVER )
	NOTE( D4, CROTCHET_DOTTED )
	# bar ...39
	delay( MINIM_DOTTED )
	# bar 40
	NOTE( E4, CROTCHET )
	NOTE( Fs4, QUAVER )
	NOTE( G4, CROTCHET_DOTTED )
	NOTE( E4, CROTCHET )

	# bar 41
	NOTE( Cs4, CROTCHET )
	NOTE( D4, QUAVER )
	NOTE( E4, CROTCHET )
	# tick picture
	NOTE( A3, QUAVER )
	NOTE( D4, QUAVER )
	NOTE( E4, QUAVER )
	# bar 42
	NOTE( F4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( D4, QUAVER )
	NOTE( C4, CROTCHET_DOTTED )

	NOTE( A3, QUAVER )
	NOTE( As3, QUAVER )
	# bar 43
	NOTE( C4, CROTCHET )
	NOTE( F4, CROTCHET )
	NOTE( E4, QUAVER )
	NOTE( D4, QUAVER )
	NOTE( D4, QUAVER )

	NOTE( C4, QUAVER )
	# bar 44
	NOTE( D4, QUAVER )
	NOTE( C4, QUAVER )

	NOTE( C4, CROTCHET )
	NOTE( C4, CROTCHET )
	NOTE( A3, QUAVER )
	NOTE( As3, QUAVER )
	# bar 45
	NOTE( C4, CROTCHET )
	NOTE( F4, CROTCHET )
	NOTE( G4, QUAVER )
	NOTE( F4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( D4, QUAVER )
	# bar 46
	NOTE( D4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( F4, CROTCHET )
	NOTE( F4, CROTCHET )
	# explosion picture
	NOTE( G4, QUAVER )
	NOTE( A4, QUAVER )
	# bar 47
	NOTE( As4, QUAVER )
	NOTE( As4, QUAVER )
	NOTE( A4, CROTCHET )
	NOTE( G4, CROTCHET )
	# Atom picture

	NOTE( F4, QUAVER )
	NOTE( G4, QUAVER )
	# bar 48
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( G4, QUAVER )
	NOTE( F4, QUAVER )
	NOTE( F4, CROTCHET )
	# Aperture picture

	NOTE( D4, QUAVER )
	NOTE( C4, QUAVER )
	# bar 49...
	NOTE( D4, QUAVER )
	NOTE( F4, QUAVER )
	NOTE( F4, QUAVER )
	NOTE( E4, CROTCHET )
	NOTE( E4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( Fs4, MINIM + QUAVER )
	# bar ...50
	delay( MINIM )
	# bar 51
	delay( MINIM )
	delay( MINIM )
	# bar 52
	delay( MINIM )
	delay( MINIM )
	# bar 53...
	delay( MINIM )
	NOTE( G4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( E4, CROTCHET )
	# bar ...54
	NOTE( Fs4, CROTCHET_DOTTED )
	delay( MINIM )
	# bar 55...
	delay( CROTCHET_DOTTED )

	NOTE( A3, QUAVER )
	NOTE( G4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( E4, CROTCHET_DOTTED )
	# bar ...56...

	NOTE( Fs4, QUAVER )
	NOTE( D4, CROTCHET_DOTTED )
	NOTE( E4, QUAVER )
	NOTE( A3, MINIM + QUAVER )
	# bar ...57
	delay( MINIM )
	# bar 58
	NOTE( E4, CROTCHET )
	NOTE( Fs4, QUAVER )
	NOTE( G4, CROTCHET_DOTTED )
	NOTE( E4, CROTCHET )
	# bar 59...
	NOTE( Cs4, CROTCHET )
	NOTE( D4, QUAVER )
	NOTE( E4, CROTCHET )
	delay( QUAVER )

	NOTE( A3, QUAVER )
	NOTE( A3, CROTCHET )
	# bar ...60
	NOTE ( Fs4, MINIM + QUAVER )
	delay( CROTCHET  )
	# bar 61...
	delay( CROTCHET  )
	# black mesa picture
	delay( CROTCHET  )
	NOTE( B4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( G4, QUAVER )
	NOTE( G4, CROTCHET )
	# bar ...62
	NOTE( A4, CROTCHET )
	delay( MINIM + QUAVER )
	# bar 63...
	delay( MINIM )

	NOTE( B4, QUAVER )

	NOTE( A4, QUAVER )

	NOTE( G4, QUAVER )

	NOTE( G4, CROTCHET_DOTTED )
	# bar ...64...

	NOTE( A4, QUAVER )
	NOTE( Fs4, CROTCHET_DOTTED )

	NOTE( G4, QUAVER )
	NOTE( D4, CROTCHET_DOTTED )
	# cake picture
	# bar ...65
	# set tempo to 135ms per beat. (slightly slower)
	delay( MINIM_DOTTED )
	# bar 66
	NOTE( E4, CROTCHET )
	NOTE( Fs4, QUAVER )
	NOTE( G4, CROTCHET_DOTTED )
	NOTE( E4, CROTCHET )
	# bar 67
	NOTE( Cs4, CROTCHET )
	NOTE( D4, QUAVER )
	NOTE( E4, CROTCHET )
	NOTE( A3, QUAVER )
	NOTE( D4, QUAVER )
	NOTE( E4, QUAVER )
	# bar 68
	NOTE( F4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( D4, QUAVER )
	# GLaDos picture
	NOTE( C4, CROTCHET_DOTTED )

	NOTE( A3, QUAVER )
	NOTE( As3, QUAVER )
	# bar 69
	NOTE( C4, CROTCHET )
	NOTE( F4, CROTCHET )
	NOTE( E4, QUAVER )
	NOTE( D4, QUAVER )
	NOTE( D4, QUAVER )
	NOTE( C4, QUAVER )
	# bar 70"
	NOTE( D4, QUAVER )
	NOTE( C4, QUAVER )
	NOTE( C4, CROTCHET )
	# aperture picture
	NOTE( C4, CROTCHET )

	NOTE( A3, QUAVER )
	NOTE( As3, QUAVER )
	# bar 71
	NOTE( C4, CROTCHET )
	NOTE( F4, CROTCHET )
	NOTE( G4, QUAVER )
	NOTE( F4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( D4, QUAVER )
	# bar 72
	NOTE( D4, QUAVER )
	NOTE( E4, QUAVER )
	NOTE( F4, CROTCHET )
	# atom picture
	NOTE( F4, CROTCHET )
	NOTE( G4, QUAVER )
	NOTE( A4, QUAVER )
	# bar 73
	NOTE( As4, QUAVER )
	NOTE( As4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( G4, QUAVER )
	# explosion picture
	NOTE( G4, CROTCHET )

	NOTE( F4, QUAVER )
	NOTE( G4, QUAVER )
	# bar 74
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( G4, QUAVER )
	NOTE( F4, QUAVER )
	# aperture picture
	NOTE( F4, CROTCHET )

	NOTE( D4, QUAVER )
	NOTE( C4, QUAVER )
	# bar 75...
	NOTE( D4, QUAVER )
	NOTE( F4, QUAVER )
	NOTE( F4, QUAVER )
	NOTE( E4, CROTCHET )
	NOTE( E4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( Fs4, MINIM + QUAVER )
	# bar...76
	# set tempo to 140ms per beat. (slightly slower)
	delay( QUAVER )    
	delay( QUAVER )    
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	# bar 77...
	NOTE( B4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( D4, CROTCHET )
	NOTE( E4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( A4, CROTCHET_DOTTED )
	# bar ...78
	# set tempo to 145ms per beat. (slightly slower)
	delay( QUAVER )    
	# set text rate to 1
	# set text rate
	delay( CROTCHET )    
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	# bar 79...
	NOTE( B4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( D4, CROTCHET )
	NOTE( G4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( A4, CROTCHET_DOTTED )
	# bar ...80
	# set tempo to 150ms per beat. (slightly slower)
	delay( QUAVER )    
	# set text rate to 1
	# set text rate
	delay( CROTCHET )
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	# bar 81...
	NOTE( B4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( D4, CROTCHET )
	NOTE( G4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( A4, CROTCHET_DOTTED )
	# bar ...82
	# set tempo to 155ms per beat. (slightly slower)
	delay( CROTCHET )
	# set text rate to 1
	# set text rate
	delay( CROTCHET )
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	# bar 83...
	NOTE( B4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( D4, CROTCHET )
	NOTE( G4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( A4, CROTCHET_DOTTED )
	#bar ...84
	# set tempo to 160ms per beat. (slightly slower)
	delay( QUAVER )
	# set text rate to 1
	# set text rate
	delay( CROTCHET )
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( A4, QUAVER )
	# bar 85...
	NOTE( B4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( D4, CROTCHET )
	NOTE( G4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( A4, CROTCHET_DOTTED )
	# bar ...86...
	# set tempo to 165ms per beat. (slightly slower)
	delay( QUAVER )

	delay( CROTCHET )

	NOTE( G4, QUAVER )
	NOTE( A4, QUAVER )
	NOTE( A4, CROTCHET_DOTTED )
	# bar ...87...
	delay( CROTCHET_DOTTED )
	NOTE( G4, QUAVER )
	NOTE( Fs4, QUAVER )
	NOTE( Fs4, MINIM + QUAVER )
	# bar ...88
	delay( MINIM )
	# delays...
	delay( MINIM_DOTTED )
	delay( MINIM_DOTTED )
	delay( MINIM_DOTTED )
	delay( MINIM_DOTTED )





if __name__ == '__main__':
	stillalive()