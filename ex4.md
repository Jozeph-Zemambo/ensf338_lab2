SECTION 4/4
1. If we could teleport to rooms then interpolation search would be the best method since we know all the information for the size of the "array" we need as well as the key, so itd be the most effecient. If we cannot teleport then linear search would be the only method
2. It would only take one step, with a "step" being a calculation of the mid point
3. This is a best case scenerio since we only needed one "step"
4. The best case scenerio is if the "key" is either the first room on the left or right so arr[hi] or arr[lo]. The worst case would be the room exactly in the middle of the sice theyd have to walk the most distance.
5. Although usually not as effeicnet since we have the floor layour memorized, we could implemnt interpolation search iteratively, and use memoization make the search more effecient.
