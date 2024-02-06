export type Event = {
	id: number;
	name: string;
	slug: string;
	description: string;
	location: string;
	start_time: string;
	end_time: string;
	image: string;
	date: string;
	volunteers: Volunteer[];
};

// this is a dummy type just for to demo Chart.JS
export type User = {
	id: number;
	age: number;
	firstName: string;
	lastName: string;
	weight: number;
	height: number;
};

export type Volunteer = {
	id: string;
	name: string;
	date_of_birth: string;
	date_created: string;
	email: string;
	contact_number: string;
};

export type Timeseries = {
	date: string;
	hours: number;
};
