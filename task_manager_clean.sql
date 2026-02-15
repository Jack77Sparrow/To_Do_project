--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO myuser;

--
-- Name: codewars_completed; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.codewars_completed (
    id integer NOT NULL,
    user_id integer NOT NULL,
    title character varying,
    slug character varying,
    completed_at timestamp with time zone NOT NULL,
    code_wars_task_id character varying NOT NULL
);


ALTER TABLE public.codewars_completed OWNER TO myuser;

--
-- Name: codewars_completed_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.codewars_completed_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.codewars_completed_id_seq OWNER TO myuser;

--
-- Name: codewars_completed_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.codewars_completed_id_seq OWNED BY public.codewars_completed.id;


--
-- Name: task_time_logs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task_time_logs (
    id integer NOT NULL,
    task_id integer NOT NULL,
    started_at timestamp without time zone NOT NULL,
    ended_at timestamp without time zone,
    duration_sec integer
);


ALTER TABLE public.task_time_logs OWNER TO myuser;

--
-- Name: task_time_logs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.task_time_logs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.task_time_logs_id_seq OWNER TO myuser;

--
-- Name: task_time_logs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.task_time_logs_id_seq OWNED BY public.task_time_logs.id;


--
-- Name: tasks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tasks (
    id integer NOT NULL,
    title text NOT NULL,
    description text,
    category character varying(20),
    difficulty character varying(20),
    priority character varying(20),
    status character varying(20) DEFAULT 'in progress'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    last_updated timestamp without time zone,
    due_to date,
    is_deleted boolean DEFAULT false NOT NULL,
    user_id integer,
    source character varying(20) DEFAULT 'user'::character varying NOT NULL,
    is_archived boolean NOT NULL
);


ALTER TABLE public.tasks OWNER TO myuser;

--
-- Name: tasks_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tasks_id_seq OWNER TO myuser;

--
-- Name: tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(60) NOT NULL,
    email character varying(50),
    created_at timestamp without time zone DEFAULT now(),
    codewars_username character varying,
    codewars_last_completed timestamp with time zone,
    last_activity_date date,
    current_streak integer DEFAULT 0 NOT NULL,
    longest_streak integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.users OWNER TO myuser;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO myuser;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: codewars_completed id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.codewars_completed ALTER COLUMN id SET DEFAULT nextval('public.codewars_completed_id_seq'::regclass);


--
-- Name: task_time_logs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_time_logs ALTER COLUMN id SET DEFAULT nextval('public.task_time_logs_id_seq'::regclass);


--
-- Name: tasks id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
2e5d354d67e0
\.


--
-- Data for Name: codewars_completed; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.codewars_completed (id, user_id, title, slug, completed_at, code_wars_task_id) FROM stdin;
1	1	The Hashtag Generator	the-hashtag-generator	2025-11-28 15:55:10.777+02	52449b062fb80683ec000024
2	1	Simple Pig Latin	simple-pig-latin	2025-11-28 15:38:17.832+02	520b9d2ad5c005041100000f
3	1	Your order,  please	your-order-please	2025-11-28 15:33:32.053+02	55c45be3b2079eccff00010f
4	1	Mexican Wave	mexican-wave	2025-11-27 17:57:11.855+02	58f5c63f1e26ecda7e000029
5	1	Write Number in Expanded Form	write-number-in-expanded-form	2025-11-26 20:59:16.052+02	5842df8ccbd22792a4000245
6	1	Valid Braces	valid-braces	2025-11-26 20:26:35.57+02	5277c8a221e209d3f6000b56
7	1	Count characters in your string	count-characters-in-your-string	2025-11-26 19:36:33.079+02	52efefcbcdf57161d4000091
8	1	Delete occurrences of an element if it occurs more than n times	delete-occurrences-of-an-element-if-it-occurs-more-than-n-times	2025-11-26 19:34:55.104+02	554ca54ffa7d91b236000023
9	1	Find the missing letter	find-the-missing-letter	2025-11-25 19:50:38.104+02	5839edaa6754d6fec10000a2
10	1	Equal Sides Of An Array	equal-sides-of-an-array	2025-11-25 19:45:56.902+02	5679aa472b8f57fb8c000047
11	1	Duplicate Encoder	duplicate-encoder	2025-11-24 16:50:17.256+02	54b42f9314d9229fd6000d9c
12	1	Isograms	isograms	2025-11-24 16:47:22.085+02	54ba84be607a92aa900000f1
13	1	Get the Middle Character	get-the-middle-character	2025-11-24 16:30:44.837+02	56747fd5cb988479af000028
14	1	You're a square!	youre-a-square	2025-11-24 16:22:52.944+02	54c27a33fb7da0db0100040e
15	1	Descending Order	descending-order	2025-11-24 16:05:43.598+02	5467e4d82edf8bbf40000155
16	1	Disemvowel Trolls	disemvowel-trolls	2025-11-24 16:02:35.217+02	52fba66badcd10859f00097e
17	1	Simple frequency sort	simple-frequency-sort	2025-11-23 22:06:52.119+02	5a8d2bf60025e9163c0000bc
18	1	Moving Zeros To The End	moving-zeros-to-the-end	2025-10-01 20:11:06.789+03	52597aa56021e91c93000cb0
19	1	Highest Scoring Word	highest-scoring-word	2025-10-01 19:58:45.131+03	57eb8fcdf670e99d9b000272
20	1	Find the unique number	find-the-unique-number-1	2025-10-01 19:51:35.814+03	585d7d5adb20cf33cb000235
21	1	Split and Join	split-and-join	2025-10-01 19:16:31.043+03	5816ead8dae5a59eaa000053
22	1	Replace With Alphabet Position	replace-with-alphabet-position	2025-09-30 16:20:16.345+03	546f922b54af40e1e90001da
23	1	Split Strings	split-strings	2025-09-30 16:14:44.675+03	515de9ae9dcfc28eb6000001
24	1	Counting Duplicates	counting-duplicates	2025-09-30 16:07:00.739+03	54bf1c2cd5b56cc47f0007a1
25	1	Does my number look big in this?	does-my-number-look-big-in-this	2025-09-30 16:01:28.441+03	5287e858c6b5a9678200083c
26	1	Find The Parity Outlier	find-the-parity-outlier	2025-09-30 15:47:50.442+03	5526fc09a1bbd946250002dc
27	1	Array.diff	array-dot-diff	2025-09-30 15:28:10.558+03	523f5d21c841566fde000009
28	1	Highest and Lowest	highest-and-lowest	2025-09-30 15:25:24.322+03	554b4ac871d6813a03000035
29	1	Square Every Digit	square-every-digit	2025-09-30 15:22:28.372+03	546e2562b03326a88e000020
30	1	Vowel Count	vowel-count	2025-09-30 15:19:32.096+03	54ff3102c1bad923760001f3
31	1	Find the odd int	find-the-odd-int	2025-09-29 20:12:16.024+03	54da5a58ea159efa38000836
32	1	Sum of two lowest positive integers	sum-of-two-lowest-positive-integers	2025-09-29 20:01:19.702+03	558fc85d8fd1938afb000014
33	1	Rot13	rot13-1	2025-08-06 22:25:14.697+03	530e15517bc88ac656000716
34	1	Extract the domain name from a URL	extract-the-domain-name-from-a-url-1	2025-08-06 18:19:24.447+03	514a024011ea4fb54200004b
35	1	Sort the odd	sort-the-odd	2025-08-06 17:51:16.433+03	578aa45ee9fd15ff4600090d
36	1	Which are  in?	which-are-in	2025-08-06 17:22:03.35+03	550554fd08b86f84fe000a58
37	1	Are they the "same"?	are-they-the-same	2025-08-06 17:11:58.519+03	550498447451fbbd7600041c
38	1	Unique In Order	unique-in-order	2025-08-06 11:54:05.18+03	54e6533c92449cc251001667
39	1	Sum of Digits / Digital Root	sum-of-digits-slash-digital-root	2025-08-06 11:07:43.358+03	541c8630095125aba6000c00
40	1	Two Sum	two-sum	2025-08-05 16:17:53.712+03	52c31f8e6605bcc646000082
41	1	Human Readable Time	human-readable-time	2025-08-05 16:03:54.603+03	52685f7382004e774f0001f7
42	1	Mumbling	mumbling	2025-08-05 15:41:07.923+03	5667e8f4e3f572a8f2000039
43	1	Persistent Bugger.	persistent-bugger	2025-08-04 12:11:09.843+03	55bf01e5a717a0d57e0000ec
44	1	Playing with digits	playing-with-digits	2025-08-04 11:44:30.971+03	5552101f47fc5178b1000050
45	1	Stop gninnipS My sdroW!	stop-gninnips-my-sdrow	2025-08-04 11:24:27.133+03	5264d2b162488dc400000001
46	1	Multiples of 3 or 5	multiples-of-3-or-5	2025-08-04 11:19:42.656+03	514b92a657cdc65150000006
47	1	Even or Odd	even-or-odd	2025-08-04 11:14:41.99+03	53da3dbb4a5168369a0000fe
428	1	Invert values	invert-values	2026-01-28 12:27:34.032+02	5899dc03bc95b1bf1b0000ad
429	1	Sum of Multiples	sum-of-multiples	2026-01-31 14:25:15.266+02	57241e0f440cd279b5000829
430	1	Simple Game	simple-game	2026-02-02 18:40:06.495+02	59831e3575ca6c8aea00003a
431	1	Arrays of cats and dogs	arrays-of-cats-and-dogs	2026-02-02 19:08:29.653+02	5a5f48f2880385daac00006c
432	1	Find the number of trailing zeros, in its binary representation , of a number.	find-the-number-of-trailing-zeros-in-its-binary-representation-of-a-number	2026-02-02 19:04:42.141+02	66e793bba4b1a6f2e8f890e5
433	1	Weight assistant	weight-assistant	2026-02-02 19:19:55.541+02	66ddde2d9d82c8517b575432
434	1	Xmas Tree	xmas-tree	2026-02-02 19:23:27.294+02	577c349edf78c178a1000108
435	1	Are there any arrows left?	are-there-any-arrows-left	2026-02-04 15:28:10.205+02	559f860f8c0d6c7784000119
436	1	Bin to Decimal	bin-to-decimal	2026-02-04 15:29:40.701+02	57a5c31ce298a7e6b7000334
\.


--
-- Data for Name: task_time_logs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task_time_logs (id, task_id, started_at, ended_at, duration_sec) FROM stdin;
48	642	2026-02-10 19:38:39.598768	2026-02-10 19:39:16.441621	37
49	642	2026-02-10 19:38:50.127185	2026-02-10 19:39:16.441621	26
39	642	2026-02-10 19:33:11.861273	2026-02-10 19:39:16.441621	365
40	642	2026-02-10 19:33:19.310583	2026-02-10 19:39:16.441621	357
41	642	2026-02-10 19:33:53.551693	2026-02-10 19:39:16.441621	323
42	642	2026-02-10 19:34:07.60784	2026-02-10 19:39:16.441621	309
43	642	2026-02-10 19:35:05.815362	2026-02-10 19:39:16.441621	251
44	642	2026-02-10 19:35:50.05482	2026-02-10 19:39:16.441621	206
45	642	2026-02-10 19:37:21.430697	2026-02-10 19:39:16.441621	115
46	642	2026-02-10 19:37:22.070718	2026-02-10 19:39:16.441621	114
47	642	2026-02-10 19:37:38.367416	2026-02-10 19:39:16.441621	98
36	667	2026-02-10 19:13:41.968929	2026-02-10 19:20:22.276434	400
37	667	2026-02-10 19:18:33.750137	2026-02-10 19:20:22.276434	109
38	667	2026-02-10 19:19:26.21367	2026-02-10 19:20:22.276434	56
\.


--
-- Data for Name: tasks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tasks (id, title, description, category, difficulty, priority, status, created_at, last_updated, due_to, is_deleted, user_id, source, is_archived) FROM stdin;
672	Array  combinations	https://www.codewars.com/kata/59e66e48fc3c499ec5000103	study	6 kyu	medium	pending	2026-02-09 21:09:14.388365	2026-02-09 21:09:14.38837	2026-02-10	f	1	codewars	f
675	Method For Counting Total Occurence Of Specific Digits	https://www.codewars.com/kata/56311e4fdd811616810000ce	study	7 kyu	medium	pending	2026-02-11 20:05:05.43469	2026-02-11 20:05:05.434697	2026-02-12	f	1	codewars	f
666	Find the number of trailing zeros, in its binary representation , of a number.	https://www.codewars.com/kata/66e793bba4b1a6f2e8f890e5	study	7 kyu	medium	overdue	2026-02-02 17:13:54.223442	2026-02-02 17:13:54.223447	2026-02-02	t	1	codewars	t
316	Practice algorithms #8	Needs to be completed before deadline	study	hard	low	overdue	2025-11-03 15:04:00	2025-11-03 15:04:00	2025-11-12	f	1	user	t
345	Practice algorithms #37	Routine task for today	study	medium	high	overdue	2025-11-21 15:04:00	2025-11-21 15:04:00	2025-11-23	f	1	user	t
346	Clean the apartment #38	Work-related responsibility	home	easy	high	overdue	2025-11-06 15:04:00	2025-11-06 15:04:00	2025-11-11	f	1	user	t
384	Prepare presentation #76	High priority personal task	study	medium	low	overdue	2025-11-07 15:04:00	2025-11-07 15:04:00	2025-11-10	f	1	user	t
386	Refactor codebase #78	Needs to be completed before deadline	work	hard	high	overdue	2025-11-09 15:04:00	2025-11-09 15:04:00	2025-11-13	f	1	user	t
387	Call parents #79	Important task that requires focus	work	medium	high	overdue	2025-12-06 15:04:00	2025-12-06 15:04:00	2025-12-15	f	1	user	t
388	Practice algorithms #80	Short task, low effort	personal	medium	medium	overdue	2025-12-14 15:04:00	2025-12-14 15:04:00	2025-12-15	f	1	user	t
390	Write unit tests #82	Needs to be completed before deadline	work	medium	medium	overdue	2025-11-04 15:04:00	2025-11-04 15:04:00	2025-11-12	f	1	user	t
391	Read technical documentation #83	Study-related activity	study	easy	high	overdue	2025-10-25 15:04:00	2025-10-25 15:04:00	2025-11-02	f	1	user	t
392	Prepare presentation #84	Important task that requires focus	study	medium	medium	overdue	2025-10-22 15:04:00	2025-10-22 15:04:00	2025-11-05	f	1	user	t
393	Prepare for interview #85	Study-related activity	study	easy	high	overdue	2025-11-09 15:04:00	2025-11-09 15:04:00	2025-11-17	f	1	user	t
394	Go to the gym #86	Short task, low effort	personal	medium	high	overdue	2025-10-16 15:04:00	2025-10-16 15:04:00	2025-10-21	f	1	user	t
395	Buy groceries #87	Work-related responsibility	home	hard	medium	overdue	2025-11-22 15:04:00	2025-11-22 15:04:00	2025-11-28	f	1	user	t
396	Go to the gym #88	Short task, low effort	personal	medium	medium	overdue	2025-11-20 15:04:00	2025-11-20 15:04:00	2025-11-25	f	1	user	t
397	Update resume #89	Important task that requires focus	work	medium	high	overdue	2025-11-05 15:04:00	2025-11-05 15:04:00	2025-11-13	f	1	user	t
398	Fix backend bug #90	Study-related activity	work	hard	high	overdue	2025-10-27 15:04:00	2025-10-27 15:04:00	2025-11-07	f	1	user	t
400	Organize workspace #92	Long-term task, plan carefully	personal	easy	low	overdue	2025-11-06 15:04:00	2025-11-06 15:04:00	2025-11-09	f	1	user	t
401	Fix backend bug #93	Routine task for today	work	medium	low	overdue	2025-12-13 15:04:00	2025-12-13 15:04:00	2025-12-24	f	1	user	t
404	Go to the gym #96	Important task that requires focus	personal	medium	low	overdue	2025-11-08 15:04:00	2025-11-08 15:04:00	2025-11-09	f	1	user	t
405	Write project report #97	Long-term task, plan carefully	work	medium	medium	overdue	2025-12-07 15:04:00	2025-12-07 15:04:00	2025-12-19	f	1	user	t
406	Organize workspace #98	Needs to be completed before deadline	home	easy	low	overdue	2025-11-27 15:04:00	2025-11-27 15:04:00	2025-12-05	f	1	user	t
408	Plan weekly schedule #100	High priority personal task	personal	medium	low	overdue	2025-11-04 15:04:00	2025-11-04 15:04:00	2025-11-07	f	1	user	t
409	Fix backend bug #101	Important task that requires focus	work	medium	high	overdue	2025-12-10 15:04:00	2025-12-10 15:04:00	2025-12-12	f	1	user	t
410	Review pull requests #102	Short task, low effort	work	medium	low	overdue	2025-11-17 15:04:00	2025-11-17 15:04:00	2025-11-25	f	1	user	t
411	Write project report #103	Work-related responsibility	work	medium	low	overdue	2025-11-18 15:04:00	2025-11-18 15:04:00	2025-11-30	f	1	user	t
412	Prepare presentation #104	High priority personal task	study	medium	medium	overdue	2025-12-10 15:04:00	2025-12-10 15:04:00	2025-12-14	f	1	user	t
441	Call parents #133	High priority personal task	personal	medium	medium	overdue	2025-11-20 15:04:00	2025-11-20 15:04:00	2025-11-25	f	1	user	t
443	Learn FastAPI #135	Important task that requires focus	work	medium	low	overdue	2025-11-19 15:04:00	2025-11-19 15:04:00	2025-11-23	f	1	user	t
444	Prepare for exam #136	Important task that requires focus	study	medium	low	overdue	2025-12-02 15:04:00	2025-12-02 15:04:00	2025-12-13	f	1	user	t
446	Finish homework #138	Long-term task, plan carefully	personal	medium	medium	overdue	2025-10-26 15:04:00	2025-10-26 15:04:00	2025-10-27	f	1	user	t
447	Practice algorithms #139	Routine task for today	study	medium	medium	overdue	2025-11-29 15:04:00	2025-11-29 15:04:00	2025-12-13	f	1	user	t
449	Study Python #141	High priority personal task	study	medium	high	overdue	2025-11-16 15:04:00	2025-11-16 15:04:00	2025-11-28	f	1	user	t
450	Write unit tests #142	Study-related activity	study	medium	high	overdue	2025-11-15 15:04:00	2025-11-15 15:04:00	2025-11-19	f	1	user	t
453	Study Python #145	Long-term task, plan carefully	study	medium	low	overdue	2025-10-20 15:04:00	2025-10-20 15:04:00	2025-10-27	f	1	user	t
454	Finish homework #146	Work-related responsibility	work	hard	high	overdue	2025-10-31 15:04:00	2025-10-31 15:04:00	2025-11-04	f	1	user	t
455	Prepare presentation #147	Maintenance and organization task	study	medium	low	overdue	2025-10-20 15:04:00	2025-10-20 15:04:00	2025-11-03	f	1	user	t
458	Go to the gym #150	Long-term task, plan carefully	personal	medium	low	overdue	2025-11-17 15:04:00	2025-11-17 15:04:00	2025-11-19	f	1	user	t
459	Practice algorithms #151	Long-term task, plan carefully	personal	medium	medium	overdue	2025-10-26 15:04:00	2025-10-26 15:04:00	2025-10-31	f	1	user	t
462	Write unit tests #154	Maintenance and organization task	work	medium	medium	overdue	2025-12-03 15:04:00	2025-12-03 15:04:00	2025-12-06	f	1	user	t
492	Update resume #184	Important task that requires focus	work	medium	high	overdue	2025-11-22 15:04:00	2025-11-22 15:04:00	2025-12-02	f	1	user	t
494	Prepare for interview #186	Long-term task, plan carefully	study	medium	high	overdue	2025-11-08 15:04:00	2025-11-08 15:04:00	2025-11-21	f	1	user	t
495	Write unit tests #187	Study-related activity	study	medium	high	overdue	2025-10-24 15:04:00	2025-10-24 15:04:00	2025-10-30	f	1	user	t
496	Update resume #188	High priority personal task	work	medium	high	overdue	2025-12-04 15:04:00	2025-12-04 15:04:00	2025-12-14	f	1	user	t
499	Study Python #191	Maintenance and organization task	study	medium	low	overdue	2025-11-18 15:04:00	2025-11-18 15:04:00	2025-11-19	f	1	user	t
500	Buy groceries #192	High priority personal task	personal	medium	low	overdue	2025-11-17 15:04:00	2025-11-17 15:04:00	2025-11-23	f	1	user	t
501	Review pull requests #193	Needs to be completed before deadline	work	medium	medium	overdue	2025-11-13 15:04:00	2025-11-13 15:04:00	2025-11-17	f	1	user	t
504	Write project report #196	Routine task for today	work	medium	low	overdue	2025-11-18 15:04:00	2025-11-18 15:04:00	2025-11-26	f	1	user	t
349	Fix backend bug #41	Work-related responsibility	work	hard	medium	overdue	2025-12-02 15:04:00	2025-12-02 15:04:00	2025-12-07	f	1	user	t
350	Practice algorithms #42	Study-related activity	study	hard	medium	overdue	2025-12-07 15:04:00	2025-12-07 15:04:00	2025-12-18	f	1	user	t
351	Buy groceries #43	Work-related responsibility	home	hard	low	overdue	2025-11-23 15:04:00	2025-11-23 15:04:00	2025-11-24	f	1	user	t
355	Study Python #47	Needs to be completed before deadline	study	hard	low	overdue	2025-10-30 15:04:00	2025-10-30 15:04:00	2025-11-09	f	1	user	t
356	Plan weekly schedule #48	Routine task for today	personal	medium	medium	overdue	2025-11-27 15:04:00	2025-11-27 15:04:00	2025-12-03	f	1	user	t
358	Clean the apartment #50	Short task, low effort	home	medium	high	overdue	2025-11-05 15:04:00	2025-11-05 15:04:00	2025-11-07	f	1	user	t
505	Read technical documentation #197	Short task, low effort	work	easy	low	overdue	2025-11-15 15:04:00	2025-11-15 15:04:00	2025-11-29	f	1	user	t
506	Study Python #198	Needs to be completed before deadline	study	hard	high	overdue	2025-12-07 15:04:00	2025-12-07 15:04:00	2025-12-14	f	1	user	t
507	Write unit tests #199	Needs to be completed before deadline	work	medium	medium	overdue	2025-11-29 15:04:00	2025-11-29 15:04:00	2025-12-10	f	1	user	t
508	Organize workspace #200	Long-term task, plan carefully	personal	easy	low	overdue	2025-11-12 15:04:00	2025-11-12 15:04:00	2025-11-26	f	1	user	t
510	Study Python #202	Long-term task, plan carefully	study	medium	high	overdue	2025-10-16 15:04:00	2025-10-16 15:04:00	2025-10-21	f	1	user	t
513	Plan weekly schedule #205	Short task, low effort	personal	medium	high	overdue	2025-12-10 15:04:00	2025-12-10 15:04:00	2025-12-22	f	1	user	t
514	Learn FastAPI #206	High priority personal task	personal	medium	high	overdue	2025-10-18 15:04:00	2025-10-18 15:04:00	2025-10-22	f	1	user	t
515	Fix backend bug #207	Important task that requires focus	work	medium	high	overdue	2025-12-10 15:04:00	2025-12-10 15:04:00	2025-12-20	f	1	user	t
516	Buy groceries #208	Needs to be completed before deadline	home	hard	low	overdue	2025-10-19 15:04:00	2025-10-19 15:04:00	2025-10-28	f	1	user	t
517	Update resume #209	High priority personal task	work	medium	medium	overdue	2025-10-20 15:04:00	2025-10-20 15:04:00	2025-10-26	f	1	user	t
518	Call parents #210	Important task that requires focus	work	medium	low	overdue	2025-12-06 15:04:00	2025-12-06 15:04:00	2025-12-18	f	1	user	t
539	Fix backend bug #231	Work-related responsibility	work	hard	medium	overdue	2025-10-25 15:04:00	2025-10-25 15:04:00	2025-11-03	f	1	user	t
540	Clean the apartment #232	Routine task for today	home	medium	high	overdue	2025-11-03 15:04:00	2025-11-03 15:04:00	2025-11-15	f	1	user	t
542	Go to the gym #234	Routine task for today	personal	medium	medium	overdue	2025-11-28 15:04:00	2025-11-28 15:04:00	2025-12-01	f	1	user	t
543	Write unit tests #235	Long-term task, plan carefully	personal	medium	low	overdue	2025-11-02 15:04:00	2025-11-02 15:04:00	2025-11-14	f	1	user	t
545	Finish homework #237	Needs to be completed before deadline	study	hard	high	overdue	2025-11-17 15:04:00	2025-11-17 15:04:00	2025-12-01	f	1	user	t
546	Prepare presentation #238	Work-related responsibility	study	medium	low	overdue	2025-12-07 15:04:00	2025-12-07 15:04:00	2025-12-19	f	1	user	t
547	Refactor codebase #239	Needs to be completed before deadline	work	hard	high	overdue	2025-11-21 15:04:00	2025-11-21 15:04:00	2025-12-05	f	1	user	t
549	Learn FastAPI #241	Needs to be completed before deadline	personal	hard	medium	overdue	2025-11-14 15:04:00	2025-11-14 15:04:00	2025-11-19	f	1	user	t
550	Prepare for interview #242	Needs to be completed before deadline	study	easy	low	overdue	2025-12-12 15:04:00	2025-12-12 15:04:00	2025-12-22	f	1	user	t
551	Fix backend bug #243	Needs to be completed before deadline	work	hard	high	overdue	2025-10-31 15:04:00	2025-10-31 15:04:00	2025-11-05	f	1	user	t
552	Finish homework #244	High priority personal task	personal	medium	low	overdue	2025-12-02 15:04:00	2025-12-02 15:04:00	2025-12-09	f	1	user	t
553	Clean the apartment #245	High priority personal task	home	medium	medium	overdue	2025-12-04 15:04:00	2025-12-04 15:04:00	2025-12-07	f	1	user	t
554	Study Python #246	Maintenance and organization task	study	medium	medium	overdue	2025-10-23 15:04:00	2025-10-23 15:04:00	2025-10-26	f	1	user	t
555	Plan weekly schedule #247	Long-term task, plan carefully	personal	medium	high	overdue	2025-10-29 15:04:00	2025-10-29 15:04:00	2025-11-02	f	1	user	t
556	Study Python #248	Important task that requires focus	study	medium	low	overdue	2025-11-09 15:04:00	2025-11-09 15:04:00	2025-11-13	f	1	user	t
557	Study Python #249	Short task, low effort	study	medium	medium	overdue	2025-11-19 15:04:00	2025-11-19 15:04:00	2025-12-02	f	1	user	t
558	Buy groceries #250	High priority personal task	personal	medium	medium	overdue	2025-11-24 15:04:00	2025-11-24 15:04:00	2025-11-27	f	1	user	t
560	Read technical documentation #252	Short task, low effort	work	easy	low	overdue	2025-10-16 15:04:00	2025-10-16 15:04:00	2025-10-28	f	1	user	t
561	Write unit tests #253	Short task, low effort	personal	medium	high	overdue	2025-11-19 15:04:00	2025-11-19 15:04:00	2025-11-25	f	1	user	t
562	Learn FastAPI #254	Routine task for today	personal	medium	medium	overdue	2025-11-30 15:04:00	2025-11-30 15:04:00	2025-12-05	f	1	user	t
566	Buy groceries #258	Routine task for today	home	medium	low	overdue	2025-12-08 15:04:00	2025-12-08 15:04:00	2025-12-15	f	1	user	t
567	Refactor codebase #259	Long-term task, plan carefully	work	medium	low	overdue	2025-11-25 15:04:00	2025-11-25 15:04:00	2025-12-05	f	1	user	t
568	Call parents #260	Work-related responsibility	work	hard	medium	overdue	2025-11-30 15:04:00	2025-11-30 15:04:00	2025-12-13	f	1	user	t
570	Buy groceries #262	Short task, low effort	home	medium	high	overdue	2025-11-17 15:04:00	2025-11-17 15:04:00	2025-11-29	f	1	user	t
572	Write unit tests #264	Long-term task, plan carefully	personal	medium	medium	overdue	2025-11-12 15:04:00	2025-11-12 15:04:00	2025-11-20	f	1	user	t
574	Practice algorithms #266	Needs to be completed before deadline	study	hard	medium	overdue	2025-10-18 15:04:00	2025-10-18 15:04:00	2025-10-28	f	1	user	t
575	Go to the gym #267	Routine task for today	personal	medium	high	overdue	2025-11-13 15:04:00	2025-11-13 15:04:00	2025-11-26	f	1	user	t
635	testtask10		personal	hard	medium	overdue	2025-12-17 17:49:00	2025-12-17 17:49:00	2025-12-18	f	1	user	t
636	w;othdvjsakl		personal	hard	medium	overdue	2025-12-17 17:49:00	2025-12-17 17:49:00	2025-12-18	f	1	user	t
310	Refactor codebase #1	something	study	hard	high	overdue	2025-11-18 15:04:00	2026-01-15 17:49:58.25469	2025-12-27	f	1	user	t
649	clean task manager code		home	medium	medium	overdue	2025-12-21 19:27:00	2025-12-21 19:27:00	2025-12-21	t	1	user	t
673	new_taskwtf	hello wathasld\nsdlfj;aslkj	personal	hard	medium	pending	2026-02-10 18:35:00.959122	2026-02-10 18:44:57.938287	\N	t	\N	user	f
361	Fix backend bug #53	Needs to be completed before deadline	work	hard	medium	overdue	2025-11-19 15:04:00	2025-11-19 15:04:00	2025-11-23	f	1	user	t
362	Call parents #54	Maintenance and organization task	work	medium	high	overdue	2025-11-07 15:04:00	2025-11-07 15:04:00	2025-11-15	f	1	user	t
363	Clean the apartment #55	Long-term task, plan carefully	home	medium	medium	overdue	2025-12-05 15:04:00	2025-12-05 15:04:00	2025-12-08	f	1	user	t
364	Study Python #56	Study-related activity	study	hard	medium	overdue	2025-10-18 15:04:00	2025-10-18 15:04:00	2025-10-22	f	1	user	t
365	Practice algorithms #57	Short task, low effort	personal	medium	high	overdue	2025-12-04 15:04:00	2025-12-04 15:04:00	2025-12-15	f	1	user	t
366	Write unit tests #58	High priority personal task	personal	medium	high	overdue	2025-10-30 15:04:00	2025-10-30 15:04:00	2025-11-01	f	1	user	t
368	Prepare presentation #60	Routine task for today	study	medium	low	overdue	2025-11-30 15:04:00	2025-11-30 15:04:00	2025-12-01	f	1	user	t
653	Test created at sorting	test hello watafa	work	medium	medium	overdue	2026-01-26 11:37:33.529713	2026-02-04 13:21:41.662055	2026-01-28	f	1	user	t
647	Learn Python	Complete the task of learni\nsdlja;ng Python programming.	study	medium	high	overdue	2025-12-17 19:34:00	2026-02-04 13:23:39.001907	2026-01-23	f	1	user	t
646	Create visual content	Develop or design visual materials as required.\nwatafo	study	hard	high	overdue	2025-12-17 19:30:00	2026-02-04 14:53:04.890082	2026-01-21	f	1	user	t
671	Sort the Unsortable	https://www.codewars.com/kata/65001dd40038a647480989c8	study	7 kyu	high	overdue	2026-02-02 19:22:09.12552	2026-02-04 13:13:46.170339	2026-02-03	f	1	codewars	t
327	Review pull requests #19	Short task, low effort	work	medium	medium	overdue	2025-11-13 15:04:00	2025-11-13 15:04:00	2025-11-20	f	1	user	t
329	Plan weekly schedule #21	Important task that requires focus	personal	medium	high	overdue	2025-11-04 15:04:00	2025-11-04 15:04:00	2025-11-15	f	1	user	t
331	Buy groceries #23	Maintenance and organization task	home	medium	high	overdue	2025-12-09 15:04:00	2025-12-09 15:04:00	2025-12-12	f	1	user	t
600	Study Python #292	Routine task for today	study	medium	low	overdue	2025-10-19 15:04:00	2025-10-19 15:04:00	2025-10-24	f	1	user	t
602	Prepare for exam #294	Long-term task, plan carefully	study	medium	high	overdue	2025-12-15 15:04:00	2025-12-15 15:04:00	2025-12-16	f	1	user	t
333	Refactor codebase #25	High priority personal task	personal	medium	low	overdue	2025-12-05 15:04:00	2025-12-05 15:04:00	2025-12-16	f	1	user	t
334	Practice algorithms #26	High priority personal task	personal	medium	high	overdue	2025-10-30 15:04:00	2025-10-30 15:04:00	2025-11-03	f	1	user	t
336	Call parents #28	Work-related responsibility	work	hard	low	overdue	2025-12-08 15:04:00	2025-12-08 15:04:00	2025-12-10	f	1	user	t
337	Finish homework #29	Needs to be completed before deadline	study	hard	medium	overdue	2025-11-22 15:04:00	2025-11-22 15:04:00	2025-11-23	f	1	user	t
340	Buy groceries #32	Routine task for today	home	medium	medium	overdue	2025-11-27 15:04:00	2025-11-27 15:04:00	2025-12-08	f	1	user	t
341	Buy groceries #33	Needs to be completed before deadline	home	hard	low	overdue	2025-11-25 15:04:00	2025-11-25 15:04:00	2025-12-02	f	1	user	t
342	Study Python #34	Needs to be completed before deadline	study	hard	high	overdue	2025-11-23 15:04:00	2025-11-23 15:04:00	2025-11-24	f	1	user	t
343	Prepare for exam #35	Routine task for today	study	medium	medium	overdue	2025-11-28 15:04:00	2025-11-28 15:04:00	2025-12-12	f	1	user	t
344	Prepare for interview #36	Maintenance and organization task	work	medium	high	overdue	2025-11-08 15:04:00	2025-11-08 15:04:00	2025-11-21	f	1	user	t
674	Most valuable character	https://www.codewars.com/kata/5dd5128f16eced000e4c42ba	study	7 kyu	medium	pending	2026-02-10 18:42:06.74715	2026-02-10 18:42:06.747155	2026-02-11	f	1	codewars	f
311	Prepare for exam #2	smakay yaiki	study	hard	low	overdue	2025-11-14 15:04:00	2026-01-15 15:23:50.508806	2025-11-29	f	1	user	t
330	Buy groceries #22	working hard	home	hard	high	overdue	2025-10-26 15:04:00	2026-01-16 13:52:06.369903	2025-10-28	f	1	user	t
312	Prepare for exam #3	smakay yaiki	study	medium	medium	overdue	2025-11-05 15:04:00	2025-11-05 15:04:00	2025-11-13	f	1	user	t
313	Update resume #5	smakay yaiki	work	easy	high	overdue	2025-12-11 15:04:00	2025-12-11 15:04:00	2025-12-23	f	1	user	t
314	Plan weekly schedule #6	smakay yaiki	personal	medium	low	overdue	2025-11-26 15:04:00	2025-11-26 15:04:00	2025-11-30	f	1	user	t
321	Fix backend bug #13	fix backend bugs 13	work	hard	medium	overdue	2025-11-17 15:04:00	2026-01-25 20:59:20.33504	2025-11-30	f	1	user	t
370	Buy groceries #62	Study-related activity	study	hard	high	overdue	2025-11-04 15:04:00	2025-11-04 15:04:00	2025-11-05	f	1	user	t
371	Prepare for interview #63	Important task that requires focus	work	medium	high	overdue	2025-11-29 15:04:00	2025-11-29 15:04:00	2025-12-09	f	1	user	t
372	Write unit tests #64	Routine task for today	work	medium	low	overdue	2025-11-24 15:04:00	2025-11-24 15:04:00	2025-12-03	f	1	user	t
374	Plan weekly schedule #66	Study-related activity	personal	easy	medium	overdue	2025-11-13 15:04:00	2025-11-13 15:04:00	2025-11-14	f	1	user	t
375	Practice algorithms #67	Study-related activity	study	hard	medium	overdue	2025-10-29 15:04:00	2025-10-29 15:04:00	2025-10-31	f	1	user	t
376	Clean the apartment #68	Work-related responsibility	home	easy	medium	overdue	2025-12-01 15:04:00	2025-12-01 15:04:00	2025-12-08	f	1	user	t
377	Read technical documentation #69	Short task, low effort	work	easy	medium	overdue	2025-11-14 15:04:00	2025-11-14 15:04:00	2025-11-18	f	1	user	t
378	Clean the apartment #70	Study-related activity	home	easy	high	overdue	2025-12-12 15:04:00	2025-12-12 15:04:00	2025-12-14	f	1	user	t
379	Read technical documentation #71	Study-related activity	study	easy	low	overdue	2025-10-19 15:04:00	2025-10-19 15:04:00	2025-11-02	f	1	user	t
381	Review pull requests #73	Study-related activity	study	medium	high	overdue	2025-12-03 15:04:00	2025-12-03 15:04:00	2025-12-14	f	1	user	t
383	Prepare for interview #75	High priority personal task	personal	medium	high	overdue	2025-10-28 15:04:00	2025-10-28 15:04:00	2025-11-07	f	1	user	t
667	Simple Game	https://www.codewars.com/kata/59831e3575ca6c8aea00003a	study	7 kyu	low	done	2026-02-02 17:30:56.585625	2026-02-04 13:17:57.542351	2026-02-03	f	1	codewars	f
414	Go to the gym #106	High priority personal task	personal	medium	high	overdue	2025-12-15 15:04:00	2025-12-15 15:04:00	2025-12-22	f	1	user	t
416	Review pull requests #108	Maintenance and organization task	work	medium	medium	overdue	2025-12-02 15:04:00	2025-12-02 15:04:00	2025-12-09	f	1	user	t
417	Write unit tests #109	Short task, low effort	personal	medium	low	overdue	2025-11-12 15:04:00	2025-11-12 15:04:00	2025-11-14	f	1	user	t
419	Call parents #111	Short task, low effort	personal	medium	medium	overdue	2025-12-12 15:04:00	2025-12-12 15:04:00	2025-12-16	f	1	user	t
420	Go to the gym #112	Routine task for today	personal	medium	low	overdue	2025-12-02 15:04:00	2025-12-02 15:04:00	2025-12-03	f	1	user	t
421	Go to the gym #113	Needs to be completed before deadline	personal	hard	medium	overdue	2025-11-20 15:04:00	2025-11-20 15:04:00	2025-12-03	f	1	user	t
424	Read technical documentation #116	High priority personal task	work	easy	medium	overdue	2025-12-14 15:04:00	2025-12-14 15:04:00	2025-12-28	f	1	user	t
425	Clean the apartment #117	Work-related responsibility	home	easy	medium	overdue	2025-12-06 15:04:00	2025-12-06 15:04:00	2025-12-18	f	1	user	t
426	Organize workspace #118	Important task that requires focus	home	medium	low	overdue	2025-10-25 15:04:00	2025-10-25 15:04:00	2025-10-29	f	1	user	t
427	Organize workspace #119	Short task, low effort	personal	medium	low	overdue	2025-11-13 15:04:00	2025-11-13 15:04:00	2025-11-19	f	1	user	t
428	Buy groceries #120	Short task, low effort	home	medium	high	overdue	2025-11-11 15:04:00	2025-11-11 15:04:00	2025-11-17	f	1	user	t
429	Refactor codebase #121	Study-related activity	study	hard	high	overdue	2025-11-01 15:04:00	2025-11-01 15:04:00	2025-11-06	f	1	user	t
430	Finish homework #122	Study-related activity	study	hard	low	overdue	2025-12-09 15:04:00	2025-12-09 15:04:00	2025-12-21	f	1	user	t
431	Prepare for interview #123	Maintenance and organization task	work	medium	low	overdue	2025-11-02 15:04:00	2025-11-02 15:04:00	2025-11-14	f	1	user	t
432	Practice algorithms #124	Routine task for today	study	medium	medium	overdue	2025-11-13 15:04:00	2025-11-13 15:04:00	2025-11-27	f	1	user	t
433	Prepare for exam #125	Needs to be completed before deadline	study	hard	low	overdue	2025-10-18 15:04:00	2025-10-18 15:04:00	2025-10-20	f	1	user	t
434	Organize workspace #126	Important task that requires focus	home	medium	low	overdue	2025-10-17 15:04:00	2025-10-17 15:04:00	2025-10-23	f	1	user	t
435	Go to the gym #127	Routine task for today	personal	medium	medium	overdue	2025-10-27 15:04:00	2025-10-27 15:04:00	2025-11-03	f	1	user	t
437	Prepare for exam #129	Maintenance and organization task	study	medium	high	overdue	2025-12-14 15:04:00	2025-12-14 15:04:00	2025-12-17	f	1	user	t
445	Update resume #137	Study-related activity	study	easy	high	overdue	2025-11-25 15:04:00	2025-11-25 15:04:00	2025-11-30	f	1	user	t
665	Solve 1 codewars kata		study	medium	medium	done	2026-01-28 13:22:15.454656	2026-01-28 13:22:15.454656	\N	t	1	codewars	f
463	Prepare for interview #155	Routine task for today	work	medium	medium	overdue	2025-11-30 15:04:00	2025-11-30 15:04:00	2025-12-11	f	1	user	t
668	Arrays of cats and dogs	https://www.codewars.com/kata/5a5f48f2880385daac00006c	study	6 kyu	medium	done	2026-02-02 19:06:49.621989	2026-02-02 19:06:49.621993	2026-02-03	f	1	codewars	f
465	Prepare for exam #157	High priority personal task	study	medium	medium	overdue	2025-11-14 15:04:00	2025-11-14 15:04:00	2025-11-28	f	1	user	t
468	Buy groceries #160	Short task, low effort	home	medium	medium	overdue	2025-11-16 15:04:00	2025-11-16 15:04:00	2025-11-25	f	1	user	t
469	Study Python #161	Routine task for today	study	medium	high	overdue	2025-11-09 15:04:00	2025-11-09 15:04:00	2025-11-11	f	1	user	t
473	Prepare for interview #165	High priority personal task	personal	medium	medium	overdue	2025-11-15 15:04:00	2025-11-15 15:04:00	2025-11-24	f	1	user	t
476	Call parents #168	Study-related activity	study	hard	medium	overdue	2025-10-17 15:04:00	2025-10-17 15:04:00	2025-10-29	f	1	user	t
477	Organize workspace #169	Study-related activity	study	easy	low	overdue	2025-12-09 15:04:00	2025-12-09 15:04:00	2025-12-22	f	1	user	t
478	Prepare for exam #170	Routine task for today	study	medium	low	overdue	2025-12-14 15:04:00	2025-12-14 15:04:00	2025-12-18	f	1	user	t
479	Go to the gym #171	Work-related responsibility	personal	hard	low	overdue	2025-11-07 15:04:00	2025-11-07 15:04:00	2025-11-11	f	1	user	t
481	Prepare for interview #173	High priority personal task	personal	medium	high	overdue	2025-11-17 15:04:00	2025-11-17 15:04:00	2025-11-22	f	1	user	t
482	Clean the apartment #174	Maintenance and organization task	home	medium	high	overdue	2025-10-16 15:04:00	2025-10-16 15:04:00	2025-10-28	f	1	user	t
484	Write project report #176	Maintenance and organization task	work	medium	low	overdue	2025-11-30 15:04:00	2025-11-30 15:04:00	2025-12-09	f	1	user	t
486	Buy groceries #178	Important task that requires focus	home	medium	medium	overdue	2025-10-30 15:04:00	2025-10-30 15:04:00	2025-11-06	f	1	user	t
487	Go to the gym #179	High priority personal task	personal	medium	low	overdue	2025-12-15 15:04:00	2025-12-15 15:04:00	2025-12-28	f	1	user	t
488	Clean the apartment #180	Routine task for today	home	medium	high	overdue	2025-10-27 15:04:00	2025-10-27 15:04:00	2025-10-30	f	1	user	t
491	Learn FastAPI #183	Work-related responsibility	work	hard	high	overdue	2025-12-02 15:04:00	2025-12-02 15:04:00	2025-12-04	f	1	user	t
521	Buy groceries #213	Maintenance and organization task	home	medium	low	overdue	2025-12-15 15:04:00	2025-12-15 15:04:00	2025-12-22	f	1	user	t
522	Finish homework #214	Short task, low effort	personal	medium	low	overdue	2025-10-23 15:04:00	2025-10-23 15:04:00	2025-11-01	f	1	user	t
523	Plan weekly schedule #215	Needs to be completed before deadline	personal	easy	medium	overdue	2025-10-18 15:04:00	2025-10-18 15:04:00	2025-10-20	f	1	user	t
669	Weight assistant	https://www.codewars.com/kata/66ddde2d9d82c8517b575432	study	6 kyu	medium	done	2026-02-02 19:17:58.480143	2026-02-02 19:17:58.480147	2026-02-03	f	1	codewars	f
524	Clean the apartment #216	Maintenance and organization task	home	medium	low	overdue	2025-10-31 15:04:00	2025-10-31 15:04:00	2025-11-13	f	1	user	t
526	Fix backend bug #218	Important task that requires focus	work	medium	medium	overdue	2025-12-09 15:04:00	2025-12-09 15:04:00	2025-12-10	f	1	user	t
527	Write unit tests #219	Important task that requires focus	work	medium	medium	overdue	2025-10-26 15:04:00	2025-10-26 15:04:00	2025-11-01	f	1	user	t
528	Learn FastAPI #220	Short task, low effort	personal	medium	medium	overdue	2025-11-24 15:04:00	2025-11-24 15:04:00	2025-12-05	f	1	user	t
531	Prepare for exam #223	Needs to be completed before deadline	study	hard	medium	overdue	2025-10-16 15:04:00	2025-10-16 15:04:00	2025-10-24	f	1	user	t
532	Study Python #224	Long-term task, plan carefully	study	medium	medium	overdue	2025-12-05 15:04:00	2025-12-05 15:04:00	2025-12-08	f	1	user	t
533	Call parents #225	Needs to be completed before deadline	personal	hard	low	overdue	2025-12-04 15:04:00	2025-12-04 15:04:00	2025-12-13	f	1	user	t
535	Refactor codebase #227	Needs to be completed before deadline	work	hard	high	overdue	2025-12-10 15:04:00	2025-12-10 15:04:00	2025-12-13	f	1	user	t
536	Update resume #228	Work-related responsibility	work	easy	medium	overdue	2025-11-16 15:04:00	2025-11-16 15:04:00	2025-11-17	f	1	user	t
576	Write unit tests #268	Short task, low effort	personal	medium	low	overdue	2025-11-06 15:04:00	2025-11-06 15:04:00	2025-11-16	f	1	user	t
579	Review pull requests #271	Routine task for today	work	medium	low	overdue	2025-11-22 15:04:00	2025-11-22 15:04:00	2025-11-24	f	1	user	t
580	Refactor codebase #272	High priority personal task	personal	medium	low	overdue	2025-12-01 15:04:00	2025-12-01 15:04:00	2025-12-06	f	1	user	t
582	Refactor codebase #274	Long-term task, plan carefully	work	medium	high	overdue	2025-11-06 15:04:00	2025-11-06 15:04:00	2025-11-16	f	1	user	t
583	Update resume #275	Long-term task, plan carefully	work	medium	medium	overdue	2025-10-21 15:04:00	2025-10-21 15:04:00	2025-10-26	f	1	user	t
585	Refactor codebase #277	Work-related responsibility	work	hard	high	overdue	2025-10-26 15:04:00	2025-10-26 15:04:00	2025-11-02	f	1	user	t
586	Read technical documentation #278	Study-related activity	study	easy	medium	overdue	2025-12-14 15:04:00	2025-12-14 15:04:00	2025-12-27	f	1	user	t
589	Fix backend bug #281	Important task that requires focus	work	medium	medium	overdue	2025-11-26 15:04:00	2025-11-26 15:04:00	2025-12-10	f	1	user	t
590	Prepare for interview #282	High priority personal task	personal	medium	high	overdue	2025-11-30 15:04:00	2025-11-30 15:04:00	2025-12-08	f	1	user	t
591	Prepare for exam #283	Needs to be completed before deadline	study	hard	low	overdue	2025-11-14 15:04:00	2025-11-14 15:04:00	2025-11-25	f	1	user	t
670	Xmas Tree	https://www.codewars.com/kata/577c349edf78c178a1000108	study	7 kyu	medium	done	2026-02-02 19:21:20.401149	2026-02-02 19:21:20.401153	2026-02-03	f	1	codewars	f
593	Clean the apartment #285	Routine task for today	home	medium	medium	overdue	2025-10-19 15:04:00	2025-10-19 15:04:00	2025-10-24	f	1	user	t
594	Prepare for interview #286	Work-related responsibility	work	easy	high	overdue	2025-11-29 15:04:00	2025-11-29 15:04:00	2025-12-13	f	1	user	t
596	Review pull requests #288	Long-term task, plan carefully	work	medium	medium	overdue	2025-11-18 15:04:00	2025-11-18 15:04:00	2025-12-02	f	1	user	t
598	Go to the gym #290	Study-related activity	study	hard	medium	overdue	2025-12-03 15:04:00	2025-12-03 15:04:00	2025-12-09	f	1	user	t
599	Learn FastAPI #291	Needs to be completed before deadline	personal	hard	low	overdue	2025-10-21 15:04:00	2025-10-21 15:04:00	2025-11-01	f	1	user	t
617	read a book		study	easy	medium	overdue	2025-12-15 20:33:00	2026-01-15 15:23:50.543935	2025-12-15	f	1	user	t
625	test3	test4	personal	hard	medium	overdue	2025-12-16 21:25:00	2025-12-16 21:25:00	2025-12-17	f	1	user	t
626	test4	test5	personal	hard	medium	overdue	2025-12-16 21:26:00	2025-12-16 21:26:00	2025-12-20	f	1	user	t
627	test5	test5	personal	hard	high	overdue	2025-12-16 21:27:00	2025-12-16 21:27:00	2025-12-28	f	1	user	t
629	test8	test8	personal	hard	medium	overdue	2025-12-16 21:33:00	2025-12-16 21:33:00	2025-12-18	f	1	user	t
631	test11	test4	personal	hard	medium	overdue	2025-12-16 21:53:00	2025-12-16 21:53:00	2025-12-08	f	1	user	t
632	lk;dsjflakj		personal	hard	medium	overdue	2025-12-16 22:03:00	2025-12-16 22:03:00	2025-12-18	f	1	user	t
633	testtask1		personal	hard	medium	overdue	2025-12-17 16:01:00	2025-12-17 16:01:00	2025-12-18	f	1	user	t
611	study python	ksadf	study	hard	medium	pending	2025-12-15 20:08:00	2026-02-04 14:07:48.366733	\N	f	1	user	f
634	testtask2		personal	hard	medium	overdue	2025-12-17 16:02:00	2025-12-17 16:02:00	2025-12-18	f	1	user	t
606	Go to the gym #298	High priority personal task	personal	medium	medium	overdue	2025-11-29 15:04:00	2025-11-29 15:04:00	2025-12-04	f	1	user	t
607	Finish homework #299	High priority personal task	personal	medium	low	overdue	2025-11-17 15:04:00	2025-11-17 15:04:00	2025-11-19	f	1	user	t
317	Fix backend bug #9	Maintenance and organization task	work	medium	high	overdue	2025-10-23 15:04:00	2025-10-23 15:04:00	2025-10-26	f	1	user	t
318	Go to the gym #10	Routine task for today	personal	medium	low	overdue	2025-11-25 15:04:00	2025-11-25 15:04:00	2025-12-05	f	1	user	t
319	Prepare for exam #11	Short task, low effort	study	medium	medium	overdue	2025-10-20 15:04:00	2025-10-20 15:04:00	2025-10-21	f	1	user	t
320	Organize workspace #12	Study-related activity	study	easy	low	overdue	2025-10-16 15:04:00	2025-10-16 15:04:00	2025-10-19	f	1	user	t
322	Prepare for interview #14	Important task that requires focus	work	medium	high	overdue	2025-12-11 15:04:00	2025-12-11 15:04:00	2025-12-25	f	1	user	t
608	Write project report #300	Routine task for today	work	medium	low	done	2025-10-16 15:04:00	2025-10-16 15:04:00	2025-10-19	f	1	user	f
325	Prepare for exam #17	High priority personal task	study	medium	high	done	2025-12-03 15:04:00	2025-12-03 15:04:00	2025-12-12	f	1	user	f
326	Write unit tests #18	Important task that requires focus	work	medium	low	done	2025-11-17 15:04:00	2025-11-17 15:04:00	2025-11-21	f	1	user	f
323	Organize workspace #15	Study-related activity	study	easy	high	overdue	2025-12-10 15:04:00	2025-12-10 15:04:00	2025-12-22	f	1	user	t
609	п		personal	hard	medium	pending	2025-12-15 20:02:00	2025-12-15 20:02:00	\N	f	1	user	f
324	Prepare for exam #16	High priority personal task	study	medium	medium	overdue	2025-11-27 15:04:00	2025-11-27 15:04:00	2025-12-09	f	1	user	t
612	update resume	update resume	work	easy	medium	overdue	2025-12-15 20:08:00	2026-01-15 15:23:50.54359	2025-12-16	f	1	user	t
610	task1		personal	hard	medium	pending	2025-12-15 20:07:00	2025-12-15 20:07:00	\N	f	1	user	f
613	create a project		work	medium	medium	pending	2025-12-15 20:15:00	2025-12-15 20:15:00	\N	f	1	user	f
614	create a project		work	medium	medium	pending	2025-12-15 20:15:00	2025-12-15 20:15:00	\N	f	1	user	f
615	make a dish		personal	hard	medium	pending	2025-12-15 20:17:00	2025-12-15 20:17:00	\N	f	1	user	f
328	Review pull requests #20	Long-term task, plan carefully	work	medium	high	done	2025-11-28 15:04:00	2025-11-28 15:04:00	2025-11-29	f	1	user	f
332	Read technical documentation #24	Maintenance and organization task	work	easy	high	done	2025-11-08 15:04:00	2025-11-08 15:04:00	2025-11-15	f	1	user	f
616	clean a house	clean a laundry 	home	easy	medium	overdue	2025-12-15 20:18:00	2026-01-15 15:23:50.543865	2025-12-16	f	1	user	t
335	Write unit tests #27	Long-term task, plan carefully	personal	medium	medium	done	2025-11-25 15:04:00	2025-11-25 15:04:00	2025-12-05	f	1	user	f
338	Write unit tests #30	Work-related responsibility	work	medium	medium	done	2025-11-08 15:04:00	2025-11-08 15:04:00	2025-11-09	f	1	user	f
339	Read technical documentation #31	Important task that requires focus	work	easy	high	done	2025-12-02 15:04:00	2025-12-02 15:04:00	2025-12-06	f	1	user	f
347	Prepare for interview #39	Important task that requires focus	work	medium	low	done	2025-10-19 15:04:00	2025-10-19 15:04:00	2025-11-01	f	1	user	f
348	Update resume #40	Short task, low effort	work	medium	low	done	2025-10-22 15:04:00	2025-10-22 15:04:00	2025-10-28	f	1	user	f
352	Learn FastAPI #44	Needs to be completed before deadline	personal	hard	medium	done	2025-12-11 15:04:00	2025-12-11 15:04:00	2025-12-21	f	1	user	f
353	Learn FastAPI #45	Study-related activity	study	hard	medium	done	2025-10-31 15:04:00	2025-10-31 15:04:00	2025-11-08	f	1	user	f
354	Learn FastAPI #46	Study-related activity	study	hard	medium	done	2025-10-22 15:04:00	2025-10-22 15:04:00	2025-11-04	f	1	user	f
357	Refactor codebase #49	Study-related activity	study	hard	low	done	2025-11-12 15:04:00	2025-11-12 15:04:00	2025-11-18	f	1	user	f
359	Prepare for interview #51	Work-related responsibility	work	easy	low	done	2025-12-08 15:04:00	2025-12-08 15:04:00	2025-12-11	f	1	user	f
360	Plan weekly schedule #52	Routine task for today	personal	medium	medium	done	2025-11-15 15:04:00	2025-11-15 15:04:00	2025-11-28	f	1	user	f
367	Learn FastAPI #59	Maintenance and organization task	work	medium	low	done	2025-11-08 15:04:00	2025-11-08 15:04:00	2025-11-19	f	1	user	f
369	Update resume #61	Maintenance and organization task	work	medium	high	done	2025-11-16 15:04:00	2025-11-16 15:04:00	2025-11-30	f	1	user	f
315	Buy groceries #7	some string	home	hard	high	done	2025-11-30 15:04:00	2026-01-24 18:29:58.984929	2025-12-06	f	1	user	f
373	Practice algorithms #65	High priority personal task	personal	medium	medium	done	2025-12-08 15:04:00	2025-12-08 15:04:00	2025-12-21	f	1	user	f
380	Finish homework #72	Important task that requires focus	work	medium	medium	done	2025-12-11 15:04:00	2025-12-11 15:04:00	2025-12-12	f	1	user	f
382	Read technical documentation #74	High priority personal task	work	easy	high	done	2025-12-04 15:04:00	2025-12-04 15:04:00	2025-12-12	f	1	user	f
385	Organize workspace #77	Long-term task, plan carefully	personal	easy	medium	done	2025-12-04 15:04:00	2025-12-04 15:04:00	2025-12-13	f	1	user	f
389	Read technical documentation #81	High priority personal task	work	easy	high	done	2025-11-19 15:04:00	2025-11-19 15:04:00	2025-11-20	f	1	user	f
399	Prepare presentation #91	Maintenance and organization task	study	medium	low	done	2025-11-26 15:04:00	2025-11-26 15:04:00	2025-12-07	f	1	user	f
402	Practice algorithms #94	Work-related responsibility	study	hard	low	done	2025-12-11 15:04:00	2025-12-11 15:04:00	2025-12-12	f	1	user	f
403	Organize workspace #95	Long-term task, plan carefully	personal	easy	high	done	2025-12-01 15:04:00	2025-12-01 15:04:00	2025-12-04	f	1	user	f
407	Study Python #99	Study-related activity	study	hard	low	done	2025-10-27 15:04:00	2025-10-27 15:04:00	2025-11-07	f	1	user	f
413	Review pull requests #105	Long-term task, plan carefully	work	medium	medium	done	2025-11-04 15:04:00	2025-11-04 15:04:00	2025-11-13	f	1	user	f
415	Buy groceries #107	Needs to be completed before deadline	home	hard	low	done	2025-11-30 15:04:00	2025-11-30 15:04:00	2025-12-12	f	1	user	f
418	Write project report #110	Short task, low effort	work	medium	low	done	2025-11-16 15:04:00	2025-11-16 15:04:00	2025-11-21	f	1	user	f
422	Read technical documentation #114	Study-related activity	study	easy	high	done	2025-10-19 15:04:00	2025-10-19 15:04:00	2025-10-22	f	1	user	f
423	Finish homework #115	High priority personal task	personal	medium	medium	done	2025-11-15 15:04:00	2025-11-15 15:04:00	2025-11-22	f	1	user	f
436	Fix backend bug #128	Important task that requires focus	work	medium	low	done	2025-10-30 15:04:00	2025-10-30 15:04:00	2025-11-04	f	1	user	f
438	Prepare for interview #130	Short task, low effort	work	medium	high	done	2025-11-08 15:04:00	2025-11-08 15:04:00	2025-11-20	f	1	user	f
439	Fix backend bug #131	High priority personal task	work	medium	medium	done	2025-11-23 15:04:00	2025-11-23 15:04:00	2025-11-25	f	1	user	f
440	Plan weekly schedule #132	Routine task for today	personal	medium	medium	done	2025-11-16 15:04:00	2025-11-16 15:04:00	2025-11-29	f	1	user	f
442	Prepare for exam #134	Needs to be completed before deadline	study	hard	high	done	2025-12-06 15:04:00	2025-12-06 15:04:00	2025-12-12	f	1	user	f
448	Prepare for interview #140	Maintenance and organization task	work	medium	high	done	2025-12-12 15:04:00	2025-12-12 15:04:00	2025-12-20	f	1	user	f
451	Organize workspace #143	Routine task for today	home	medium	low	done	2025-10-17 15:04:00	2025-10-17 15:04:00	2025-10-27	f	1	user	f
452	Clean the apartment #144	Short task, low effort	home	medium	medium	done	2025-11-15 15:04:00	2025-11-15 15:04:00	2025-11-20	f	1	user	f
456	Fix backend bug #148	Work-related responsibility	work	hard	high	done	2025-10-22 15:04:00	2025-10-22 15:04:00	2025-11-05	f	1	user	f
457	Prepare for exam #149	Maintenance and organization task	study	medium	high	done	2025-12-10 15:04:00	2025-12-10 15:04:00	2025-12-20	f	1	user	f
460	Study Python #152	High priority personal task	study	medium	high	done	2025-10-19 15:04:00	2025-10-19 15:04:00	2025-10-30	f	1	user	f
461	Prepare presentation #153	Important task that requires focus	study	medium	low	done	2025-10-31 15:04:00	2025-10-31 15:04:00	2025-11-14	f	1	user	f
464	Organize workspace #156	Study-related activity	study	easy	high	done	2025-11-06 15:04:00	2025-11-06 15:04:00	2025-11-19	f	1	user	f
466	Write project report #158	Work-related responsibility	work	medium	low	done	2025-12-02 15:04:00	2025-12-02 15:04:00	2025-12-12	f	1	user	f
467	Practice algorithms #159	Long-term task, plan carefully	personal	medium	high	done	2025-12-13 15:04:00	2025-12-13 15:04:00	2025-12-20	f	1	user	f
470	Practice algorithms #162	High priority personal task	personal	medium	medium	done	2025-12-04 15:04:00	2025-12-04 15:04:00	2025-12-09	f	1	user	f
471	Write project report #163	Important task that requires focus	work	medium	low	done	2025-10-27 15:04:00	2025-10-27 15:04:00	2025-10-30	f	1	user	f
472	Prepare for interview #164	Needs to be completed before deadline	study	easy	low	done	2025-10-29 15:04:00	2025-10-29 15:04:00	2025-11-01	f	1	user	f
474	Learn FastAPI #166	Study-related activity	study	hard	low	done	2025-10-30 15:04:00	2025-10-30 15:04:00	2025-11-02	f	1	user	f
475	Write project report #167	Important task that requires focus	work	medium	medium	done	2025-11-12 15:04:00	2025-11-12 15:04:00	2025-11-25	f	1	user	f
480	Write project report #172	Needs to be completed before deadline	work	medium	high	done	2025-11-17 15:04:00	2025-11-17 15:04:00	2025-11-18	f	1	user	f
483	Clean the apartment #175	Short task, low effort	home	medium	medium	done	2025-10-26 15:04:00	2025-10-26 15:04:00	2025-10-29	f	1	user	f
485	Plan weekly schedule #177	Long-term task, plan carefully	personal	medium	medium	done	2025-12-05 15:04:00	2025-12-05 15:04:00	2025-12-19	f	1	user	f
489	Finish homework #181	Routine task for today	work	medium	medium	done	2025-10-20 15:04:00	2025-10-20 15:04:00	2025-11-02	f	1	user	f
490	Fix backend bug #182	Long-term task, plan carefully	work	medium	medium	done	2025-12-06 15:04:00	2025-12-06 15:04:00	2025-12-09	f	1	user	f
493	Write project report #185	Maintenance and organization task	work	medium	high	done	2025-11-09 15:04:00	2025-11-09 15:04:00	2025-11-18	f	1	user	f
497	Write project report #189	High priority personal task	work	medium	low	done	2025-11-28 15:04:00	2025-11-28 15:04:00	2025-12-09	f	1	user	f
498	Learn FastAPI #190	Needs to be completed before deadline	personal	hard	low	done	2025-11-06 15:04:00	2025-11-06 15:04:00	2025-11-08	f	1	user	f
502	Plan weekly schedule #194	Maintenance and organization task	personal	medium	high	done	2025-11-07 15:04:00	2025-11-07 15:04:00	2025-11-15	f	1	user	f
503	Practice algorithms #195	Study-related activity	study	hard	high	done	2025-10-31 15:04:00	2025-10-31 15:04:00	2025-11-02	f	1	user	f
509	Clean the apartment #201	Long-term task, plan carefully	home	medium	low	done	2025-12-06 15:04:00	2025-12-06 15:04:00	2025-12-11	f	1	user	f
511	Go to the gym #203	Study-related activity	study	hard	low	done	2025-11-04 15:04:00	2025-11-04 15:04:00	2025-11-16	f	1	user	f
512	Plan weekly schedule #204	Work-related responsibility	personal	easy	low	done	2025-11-28 15:04:00	2025-11-28 15:04:00	2025-12-07	f	1	user	f
519	Finish homework #211	Maintenance and organization task	work	medium	low	done	2025-10-25 15:04:00	2025-10-25 15:04:00	2025-10-31	f	1	user	f
520	Finish homework #212	Short task, low effort	personal	medium	high	done	2025-10-23 15:04:00	2025-10-23 15:04:00	2025-11-06	f	1	user	f
525	Learn FastAPI #217	Short task, low effort	personal	medium	medium	done	2025-11-02 15:04:00	2025-11-02 15:04:00	2025-11-09	f	1	user	f
529	Organize workspace #221	Work-related responsibility	home	easy	low	done	2025-11-29 15:04:00	2025-11-29 15:04:00	2025-12-12	f	1	user	f
530	Plan weekly schedule #222	Study-related activity	personal	easy	low	done	2025-11-22 15:04:00	2025-11-22 15:04:00	2025-11-30	f	1	user	f
534	Read technical documentation #226	High priority personal task	work	easy	high	done	2025-11-26 15:04:00	2025-11-26 15:04:00	2025-11-28	f	1	user	f
537	Prepare for exam #229	Important task that requires focus	study	medium	low	done	2025-12-11 15:04:00	2025-12-11 15:04:00	2025-12-13	f	1	user	f
538	Write project report #230	Study-related activity	work	medium	high	done	2025-10-30 15:04:00	2025-10-30 15:04:00	2025-11-10	f	1	user	f
541	Buy groceries #233	Study-related activity	study	hard	high	done	2025-11-28 15:04:00	2025-11-28 15:04:00	2025-12-05	f	1	user	f
544	Practice algorithms #236	Important task that requires focus	study	medium	high	done	2025-10-28 15:04:00	2025-10-28 15:04:00	2025-11-01	f	1	user	f
548	Practice algorithms #240	Study-related activity	study	hard	low	done	2025-11-24 15:04:00	2025-11-24 15:04:00	2025-11-29	f	1	user	f
559	Write unit tests #251	Important task that requires focus	work	medium	medium	done	2025-12-06 15:04:00	2025-12-06 15:04:00	2025-12-14	f	1	user	f
563	Prepare for interview #255	Important task that requires focus	work	medium	medium	done	2025-11-06 15:04:00	2025-11-06 15:04:00	2025-11-15	f	1	user	f
564	Fix backend bug #256	High priority personal task	work	medium	low	done	2025-10-26 15:04:00	2025-10-26 15:04:00	2025-11-04	f	1	user	f
565	Study Python #257	Work-related responsibility	study	hard	low	done	2025-10-19 15:04:00	2025-10-19 15:04:00	2025-10-27	f	1	user	f
569	Practice algorithms #261	Routine task for today	study	medium	medium	done	2025-10-16 15:04:00	2025-10-16 15:04:00	2025-10-23	f	1	user	f
571	Update resume #263	Needs to be completed before deadline	work	easy	medium	done	2025-10-22 15:04:00	2025-10-22 15:04:00	2025-11-02	f	1	user	f
573	Learn FastAPI #265	Work-related responsibility	work	hard	medium	done	2025-12-13 15:04:00	2025-12-13 15:04:00	2025-12-14	f	1	user	f
577	Read technical documentation #269	Routine task for today	work	easy	low	done	2025-11-25 15:04:00	2025-11-25 15:04:00	2025-11-27	f	1	user	f
578	Review pull requests #270	High priority personal task	work	medium	high	done	2025-12-06 15:04:00	2025-12-06 15:04:00	2025-12-17	f	1	user	f
581	Prepare for exam #273	Routine task for today	study	medium	medium	done	2025-10-16 15:04:00	2025-10-16 15:04:00	2025-10-18	f	1	user	f
584	Update resume #276	Study-related activity	study	easy	medium	done	2025-11-11 15:04:00	2025-11-11 15:04:00	2025-11-25	f	1	user	f
587	Learn FastAPI #279	Long-term task, plan carefully	personal	medium	high	done	2025-11-11 15:04:00	2025-11-11 15:04:00	2025-11-22	f	1	user	f
588	Fix backend bug #280	Work-related responsibility	work	hard	high	done	2025-11-21 15:04:00	2025-11-21 15:04:00	2025-12-01	f	1	user	f
592	Review pull requests #284	Long-term task, plan carefully	work	medium	high	done	2025-10-17 15:04:00	2025-10-17 15:04:00	2025-10-23	f	1	user	f
595	Study Python #287	Study-related activity	study	hard	medium	done	2025-12-03 15:04:00	2025-12-03 15:04:00	2025-12-09	f	1	user	f
597	Buy groceries #289	Routine task for today	home	medium	high	done	2025-10-16 15:04:00	2025-10-16 15:04:00	2025-10-27	f	1	user	f
601	Organize workspace #293	Needs to be completed before deadline	home	easy	medium	done	2025-11-19 15:04:00	2025-11-19 15:04:00	2025-12-02	f	1	user	f
605	Plan weekly schedule #297	Work-related responsibility	personal	easy	high	done	2025-12-09 15:04:00	2025-12-09 15:04:00	2025-12-23	f	1	user	f
620	create a project	web project	work	medium	medium	pending	2025-12-15 21:49:00	2025-12-15 21:49:00	\N	f	1	user	f
621	clean a house	clean a laudry	home	easy	medium	pending	2025-12-15 21:54:00	2025-12-15 21:54:00	\N	f	1	user	f
622	make a profil for my project	make a profile for my project\r\n\r\nwrite html and css\r\nconnect to FastAPI 	work	medium	medium	pending	2025-12-16 21:17:00	2025-12-16 21:17:00	\N	f	1	user	f
623	test1	test1	personal	hard	medium	pending	2025-12-16 21:20:00	2025-12-16 21:20:00	\N	f	1	user	f
624	test2	test2	personal	hard	medium	pending	2025-12-16 21:22:00	2025-12-16 21:22:00	\N	f	1	user	f
628	test7	test7	personal	hard	high	done	2025-12-16 21:33:00	2025-12-16 21:33:00	2025-12-30	f	1	user	f
630	test4	test	work	medium	medium	pending	2025-12-16 21:43:00	2025-12-16 21:43:00	\N	f	1	user	f
637	Great task, learn fast happy	A great task focused on learning quickly and with enthusiasm.	work	medium	high	in progress	2025-12-17 19:06:00	2025-12-17 19:06:00	\N	f	1	user	f
638	Learn fast Abbey	Focus on quickly learning about Abbey	study	hard	high	in progress	2025-12-17 19:13:00	2025-12-17 19:13:00	\N	f	1	user	f
639	Great task Learn FastAbit	This task involves mastering the FastAbit learning module efficiently.	work	medium	high	in progress	2025-12-17 19:14:00	2025-12-17 19:14:00	\N	f	1	user	f
640	Great task Leon was stated, ready to hide	This task involves preparing and setting up the necessary steps as indicated by Leon.	work	medium	high	in progress	2025-12-17 19:16:00	2025-12-17 19:16:00	\N	f	1	user	f
641	This is the opk voice helpercess	Task related to the opk voice helpercess	work	medium	high	in progress	2025-12-17 19:19:00	2025-12-17 19:19:00	\N	f	1	user	f
643	Finish voice helper	Complete the development or improvement of the voice helper feature.	work	hard	high	in progress	2025-12-17 19:23:00	2025-12-17 19:23:00	\N	f	1	user	f
644	Finish voice help	Complete the voice help feature as planned.\nfinish	work	hard	medium	in progress	2025-12-17 19:28:00	2026-02-10 18:10:10.584278	\N	t	1	user	f
642	Voice helper task	Create a task related to the voice helper feature.\nfinish	work	medium	high	in progress	2025-12-17 19:22:00	2026-02-04 14:06:12.586704	\N	f	1	user	f
648	Learn HTML	Complete the task of learning HTML.\nand write some script\nhello watafa\nhello watafa dota2	study	medium	high	overdue	2025-12-17 19:36:00	2026-02-04 14:50:17.187336	2026-02-04	f	1	user	t
645	Finish home tasks	Complete all necessary tasks related to the home.finish\nfinish watafa	home	medium	high	overdue	2025-12-17 19:29:00	2026-02-04 14:52:01.485464	2026-02-04	f	1	user	t
603	Organize workspace #295	Long-term task, plan carefully	personal	easy	medium	overdue	2025-12-03 15:04:00	2025-12-03 15:04:00	2025-12-09	f	1	user	t
604	Finish homework #296	High priority personal task	personal	medium	high	overdue	2025-12-10 15:04:00	2025-12-10 15:04:00	2025-12-23	f	1	user	t
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, email, created_at, codewars_username, codewars_last_completed, last_activity_date, current_streak, longest_streak) FROM stdin;
1	Drake	max.brawl2001@gmail.com	2026-01-26 18:01:40.292096	MaksymParfeniuk	2026-02-04 15:29:40.701+02	2026-02-18	5	5
\.


--
-- Name: codewars_completed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.codewars_completed_id_seq', 436, true);


--
-- Name: task_time_logs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.task_time_logs_id_seq', 49, true);


--
-- Name: tasks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tasks_id_seq', 675, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 2, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: codewars_completed codewars_completed_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.codewars_completed
    ADD CONSTRAINT codewars_completed_pkey PRIMARY KEY (id);


--
-- Name: task_time_logs task_time_logs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_time_logs
    ADD CONSTRAINT task_time_logs_pkey PRIMARY KEY (id);


--
-- Name: tasks tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);


--
-- Name: codewars_completed uq_user_codewars_kata; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.codewars_completed
    ADD CONSTRAINT uq_user_codewars_kata UNIQUE (user_id, code_wars_task_id);


--
-- Name: users users_codewars_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_codewars_username_key UNIQUE (codewars_username);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: codewars_completed codewars_completed_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.codewars_completed
    ADD CONSTRAINT codewars_completed_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: task_time_logs task_time_logs_task_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_time_logs
    ADD CONSTRAINT task_time_logs_task_id_fkey FOREIGN KEY (task_id) REFERENCES public.tasks(id);


--
-- Name: tasks tasks_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

