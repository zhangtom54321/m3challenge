"""
Problem 2: In it for the long haul
"""
# Finds the cumulative distribution function
def cdf(vector, miles, beg, end):
    x = np.arange(len(miles))
    total = 0
    index = 0
    for i in range(int(beg * 10) , int(end * 10)):
        dx = np.interp(i/10, miles, vector)
        dx1 = np.interp((i + 1)/10, miles, vector)
        total += abs(dx1 - dx)
        index += 1
    return total

# Main function
def main(path, D_CONSTANT, N):
    df = pd.read_csv(path)
    df = df.dropna(axis = 1)
    df.columns = ['marker1', 'marker2', 'traffic', 'truck', 'percentage']
    df['distances'] = df['marker2'].diff()
    df = df[(df['distances'] >= 0)]
    df = df.fillna(0)
    miles = np.array(df['distances'])
    miles = np.cumsum(miles)
    truck = np.array(df['truck'])
    np.cumsum(truck)
    # want like...D/2, D, 3D/2 and then find cumsum
    TOTAL_DISTANCE = np.sum(miles)
    #D_CONSTANT = 205
    new_const = D_CONSTANT / N
    iterations = int(max(miles)/new_const)
    beginning = 0
    beg = []
    answers = []
    for i in range(0, iterations + 1):
        area = cdf(truck, miles, beginning, beginning + new_const)
        answers.append(area)
        beg.append(beginning)
        beginning = beginning + new_const
    area = cdf(truck, miles, beginning, TOTAL_DISTANCE)
    beg.append(max(miles))
    answers.append(area)
    return(np.array(answers)/128, beg)

if __name__ == "__main__":
    main()
