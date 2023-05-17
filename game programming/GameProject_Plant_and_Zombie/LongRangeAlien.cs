using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class LongRangeAlien : Alien
{
    //���� ����// Collider
    private Collider attackRangeCollider;

    private int longRangeAlienHP;
    public float attackRangeSize = 2.0f;

    protected override void Start()
    {
        base.Start();
        attackRangeCollider = GetComponentInChildren<Collider>();

    }

}
