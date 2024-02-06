import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";
import { cubicOut } from "svelte/easing";
import type { TransitionConfig } from "svelte/transition";
import { TRUNCATE_AT_CHAR } from "$lib/config";

export function cn(...inputs: ClassValue[]) {
	return twMerge(clsx(inputs));
}

type FlyAndScaleParams = {
	y?: number;
	x?: number;
	start?: number;
	duration?: number;
};

export const flyAndScale = (
	node: Element,
	params: FlyAndScaleParams = { y: -8, x: 0, start: 0.95, duration: 150 }
): TransitionConfig => {
	const style = getComputedStyle(node);
	const transform = style.transform === "none" ? "" : style.transform;

	const scaleConversion = (
		valueA: number,
		scaleA: [number, number],
		scaleB: [number, number]
	) => {
		const [minA, maxA] = scaleA;
		const [minB, maxB] = scaleB;

		const percentage = (valueA - minA) / (maxA - minA);
		const valueB = percentage * (maxB - minB) + minB;

		return valueB;
	};

	const styleToString = (
		style: Record<string, number | string | undefined>
	): string => {
		return Object.keys(style).reduce((str, key) => {
			if (style[key] === undefined) return str;
			return str + `${key}:${style[key]};`;
		}, "");
	};

	return {
		duration: params.duration ?? 200,
		delay: 0,
		css: (t) => {
			const y = scaleConversion(t, [0, 1], [params.y ?? 5, 0]);
			const x = scaleConversion(t, [0, 1], [params.x ?? 0, 0]);
			const scale = scaleConversion(t, [0, 1], [params.start ?? 0.95, 1]);

			return styleToString({
				transform: `${transform} translate3d(${x}px, ${y}px, 0) scale(${scale})`,
				opacity: t,
			});
		},
		easing: cubicOut,
	};
};

// produce a shorter even description if it's too lengthy
export function truncateDescriptionIfTooLong(description: string): string {
	if (description.length < TRUNCATE_AT_CHAR) {
		return description;
	}
	return description.slice(0, TRUNCATE_AT_CHAR) + "...";
}

export function createISOString(
	dateString: string,
	timeString: string
): string {
	// Parse date and time strings
	const dateArray = dateString.split("-").map(Number);
	const timeArray = timeString.split(":").map(Number);

	// Create a new Date object
	const isoDate = new Date(
		dateArray[0], // Year
		dateArray[1] - 1, // Month (months are 0-indexed in JavaScript)
		dateArray[2], // Day
		timeArray[0], // Hours
		timeArray[1] // Minutes
	);

	isoDate.setHours(isoDate.getHours() + 8);

	return isoDate.toISOString();
}
