export type Event = {
	id: number;
	name: string;
	slug: string;
	description: string;
	location: string;
	start_time: string;
	end_time: string;
	date: string;
	volunteers: Volunteer[];
	image?: string;
	google_form_url?: string;
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

export type Response = {
	id: string;
	email: string;
	submit_date: string;
	content: string;
	satisfaction: number;
	reason: string;
};
