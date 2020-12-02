def convert(number):
	# define the sound for each factor
	sound_dict = {
		3: 'Pling',
		5: 'Plang',
		7: 'Plong'
	}

	# loop through dict to define the sounds
	sound_str = ''
	for num, sound in sound_dict.items():
		if number % num != 0:
			continue
		else:
			sound_str += sound

	# if string is empty, return number
	if not sound_str:
		sound_str = str(number)

	return sound_str
