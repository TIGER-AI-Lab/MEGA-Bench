# Task: wikihow_complex_task_completion

## Task Description:

```
You are a multi-modal AI assistant. Given a series of images that explains how-to do something, your goal is to write down details steps to accomplish each sub-task, and finally achieve the goal.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](p1i1.png)

![Image](p1i2.png)

![Image](p1i3.png)

![Image](p1i4.png)

![Image](p1i5.png)

![Image](p1i6.png)

![Image](p1i7.png)

![Image](p1i8.png)

![Image](p1i9.png)

![Image](p1i10.png)

![Image](p1i11.png)

```
Example Question: Look at the images, write down 11 steps (in two parts) on how to propagate Elephant Ear plants. Note that image 1 to 5 are part 1 and image 6 to 11 are part 2.
Example Response: Answer: Part 1. Dividing Elephant Ear Tubers

- **Step 1. Dig up your parent plant in the fall for the highest chance of success.** For best results, wait until the parent plant starts to go dormant in the fall and the leaves start to die off before removing it from its pot or in-ground location. Dividing the new tubers from the original growth in the fall puts less stress on the parent plant because it won’t be actively growing, giving you a better chance of successfully separating the new tubers without harming the parent plant
- **Step 2. Soak your tools with bleach to avoid transferring diseases.** First, mix 1 part bleach with 9 parts water in a clean bucket. Place your pruning knife and shovel (if you’re using one) in the solution. Let the tools soak in the solution for 30 minutes, then rinse them with clean water before using them to dig up and cut new growth tubers from your parent plant
- **Step 3. Remove the parent plant from its pot or in-ground location.** If your elephant ear plant is in a pot, carefully grab onto the stems to lift it up out of its pot. If it’s planted in the ground, use your hands or a shovel to dig around the plant to loosen the soil, then grab the stems to lift it out of the ground
- **Step 4. Select healthy tubers with roots to divide from the parent plant.** First, gently shake the plant or use your hands to loosen and brush off the soil so you can see the tubers (bulbs). Then, examine the new growth tubers to see which ones are sprouting roots. As long as the tubers have at least one new root bud or sprout, they’ll likely be able to survive away from the parent plant
- **Step 5. Separate the new tubers from the parent plant.** Carefully untangle and cut away the new tuber’s roots from the parent plant tuber’s roots. Then, use a sharp knife to cut the new tubers away from the parent plant tuber wherever they intersect

Part 2. Replanting the Tubers
- **Step 1. Plant the tubers indoors if you want to grow them immediately.** You can replant the tubers immediately if you want to put them in a container. Select a large pot with drainage holes and fill it with well-draining potting soil. Make a well in the soil a little larger than the tuber and place the tuber in the well with the pointy side facing up. Lightly pack soil around the tuber and water it gently
- **Step 2. Keep the tubers in a cool, dark place until spring if you want to plant them outside.** If you live in an area with cold winters, store your elephant ear tubers inside until spring. Place each tuber in a separate paper bag and put the bags in a cool, dark place that stays dry until the weather warms up. A basement is often a good choice, as long as it’s not too humid.
- **Step 3. Select a planting location with full sun to part shade.** Elephant ear plants are jungle plants, so they do best in areas with plenty of sunlight. Avoid planting them beneath trees or structures that provide lots of shade. Ideally, plant elephant ears in areas that get 6 or more hours of sun per day
- **Step 4. Plant the tubers outdoors once temperatures reach 40 °F (4 °C) and higher.** If you’ve stored the tubers indoors through the winter or if you live in a warm location, you can safely plant your tubers outdoors. Use a shovel to dig a hole for each tuber that’s about 5 inches (13 cm) deep. Place each tuber inside the hole with its pointy side up. Cover the tuber with soil, then water it thoroughly with the hose
- **Step 5. Space the elephant ears 3–6 ft (0.91–1.83 m) apart.** Elephant ears are rather large plants, so each tuber needs plenty of space. Avoid planting them close together, or they’ll fail to thrive
- **Step 6. Keep the soil around your plants consistently moist.** Elephant ear plants need moist, but not soaking wet, soil. Plan to water your plants each morning after checking the soil with your finger to see if it’s dry about 2–3 inches (5.1–7.6 cm) deep. Water the soil around the base of the plant rather than the leaves
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 551
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning
- **App**: Planning
- **Input Format**: Artistic and Creative Content
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
